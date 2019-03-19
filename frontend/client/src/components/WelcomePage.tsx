import * as React from 'react';
export default class WelcomePage extends React.Component<any, any> {

  constructor() {
    super();
  }

  render() {
    return (
      <span>
        <h2>Welcome</h2>
        <div className='row'>
          <div className='col-md-12'>
            <img className='img-responsive' src='/images/pets.png' />
          </div>
        </div>
      </span>
    );
  }

}
