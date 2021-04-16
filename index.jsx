import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import 'babel-polyfill';
import ToggleButton from './comp-toggle-button';
import FilterCard from './comp-filter-card-body';
import ErrorBoundary from './comp-error-boundary';
import DB from './db.json';
import 'spectre.css';
import './_filters.scss';
import './_custom.scss';

const Loading = () => (
  <div className="loading loading-lg loading-position"></div>
);

const App = () => {
  const [data, setData] = useState([]);
  const [catalogList, setCatalogList] = useState([]);
  const fetchData = () => {
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
  }, []);
  const handelToggleDarkMode = () => {
    var element = document.body;
    element.classList.toggle('dark-mode');
  };
  return (
    <>
      <div className="nav">
        <button className="btn btn-sm" onClick={handelToggleDarkMode}>
          Toggle Mode
        </button>
      </div>
      {!data.length ? (
        <Loading />
      ) : (
        <div className="column col-12">
          <div className="filter">
            <ToggleButton catalogList={catalogList} />
            <div className="divider-space"></div>
            <FilterCard data={data} catalogList={catalogList} />
          </div>
        </div>
      )}
    </>
  );
};

ReactDOM.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
  document.getElementById('root'),
);
