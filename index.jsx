import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import 'spectre.css';
import ToggleButton from './comp-toggle-button';
import FilterCard from './comp-filter-card-body';
import ErrorBoundary from './comp-error-boundary';
import 'babel-polyfill';
import './_filters.scss';
import './_custom.scss';
import './custom.css';

const Loading = () => (
  <div className="loading loading-lg loading-position"></div>
);

const App = () => {
  const [data, setData] = useState([]);
  const [count, setCount] = useState(0);
  const [catalogList, setCatalogList] = useState([]);

  const fetchData = async () => {
    const response = await fetch('./db.json');
    const DB = await response.json();
    const { all } = DB;
    const data = Object.entries(all).map(([key, value]) => ({
      id: key,
      value,
    }));
    const catalogList = data
      .map(v => v.value.catalog)
      .filter((el, idx, arr) => idx === arr.indexOf(el))
      .sort();
    setCatalogList(
      ['all', ...catalogList].map((v, id) => ({
        name: v,
        idx: id,
      })),
    );
    setData(data);
  };

  useEffect(() => {
    fetchData();
  }, [count]);

  const handelToggleDarkMode = () => {
    var element = document.body;
    element.classList.toggle('dark-mode');
  };

  const handelRefresh = () => {
    setCount(c => c + 1);
  };

  if (!data.length) {
    return <Loading />;
  }

  return (
    <>
      <div className="nav">
        <div>
          <button
            className="btn btn-sm"
            onClick={handelToggleDarkMode}
            style={{ marginRight: '20px' }}
          >
            Toggle Mode
          </button>
          <button className="btn btn-sm" onClick={handelRefresh}>
            Refresh
          </button>
        </div>
      </div>
      <div className="column col-12">
        <div className="filter">
          <ToggleButton catalogList={catalogList} />
          <div className="divider-space"></div>
          <FilterCard data={data} catalogList={catalogList} />
        </div>
      </div>
    </>
  );
};

ReactDOM.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
  document.getElementById('root'),
);
