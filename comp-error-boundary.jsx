import React from 'react';

export default class ErrorBoundary extends React.Component {
  state = {
    error: null,
  };
  static getDerivedStateFromError(error) {
    return { error: error };
  }

  componentDidCatch(error, info) {
    console.log('error: ', error);
    console.log('info: ', info);
  }
  render() {
    if (this.state.error) {
      return <p>Something broke</p>;
    }
    return this.props.children;
  }
}
