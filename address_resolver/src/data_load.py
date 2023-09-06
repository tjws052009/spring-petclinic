import csv, json, os, sys, argparse, time, re
from elasticsearch import Elasticsearch
from elasticsearch.helpers import parallel_bulk

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file', required=False, default='../sample.csv')
parser.add_argument('--index', dest='index', required=False, default='address')
parser.add_argument('--es_host', dest='es_host', required=False, default=os.environ['ELASTICSEARCH_URL'])
parser.add_argument('--es_user', dest='es_user', required=False, default=os.environ['ELASTICSEARCH_USERNAME'])
parser.add_argument('--es_password', dest='es_password', required=False, default=os.environ['ELASTICSEARCH_PASSWORD'])
parser.add_argument('--thread_count', dest='thread_count', required=False, default=8, type=int)
parser.add_argument('--chunk_size', dest='chunk_size', required=False, default=1000, type=int)
parser.add_argument('--timeout', dest='timeout', required=False, default=120,type=int)
parser.add_argument('--pipeline', dest='pipeline', required=False)


def handle_data_file(file_path, index):
    with open(file_path, 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            doc = dict(row)
            doc['_index'] = index
#            doc['_type'] = "doc"
            doc = {k: v for k, v in doc.items() if v is not None and v != ""}
            yield doc


if __name__ == '__main__':
    args = parser.parse_args()
    # Add port 443 if no port is defined
    p = '(?:http.*://)?(?P<host>[^:/ ]+).?(?P<port>[0-9]*).*'
    m = re.search(p,args.es_host)
    es_host = args.es_host + ':443' if (m.group('port') == '') else args.es_host
    es = Elasticsearch(hosts=[es_host], http_auth=(args.es_user, args.es_password), verify_certs=True, timeout=args.timeout)
    start = time.time()
    if (not es.indices.exists(index=args.index)):
        es.indices.create(index=args.index, body = json.loads(open('mapping.json').read()))
    cnt = 0
    indices=set()
    for success, info in parallel_bulk(
            es,
            handle_data_file(args.file, args.index),
            thread_count=args.thread_count,
            chunk_size=args.chunk_size,
            timeout='%ss' % args.timeout,
            pipeline=args.pipeline
    ):
        if success:
            cnt += 1
            if cnt % args.chunk_size == 0:
                print('Indexed %s documents' % str(cnt), flush=True)
                sys.stdout.flush()
        else:
            print('Doc failed', info)
    print('DONE\nIndexed %s documents in %.2f seconds' % (
        cnt, time.time() - start
    ), flush=True)
    print('INDEXING COMPLETE',flush=True)
    es.indices.refresh(index=args.index)
    print('DATA LOAD COMPLETE',flush=True)
