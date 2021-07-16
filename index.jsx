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
import './custom.css';

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

  const fetchData2 = async () => {
    // const r1 = await fetch('./a.json', {
    //   headers: {
    //     'Content-Type': 'application/json',
    //     Accept: 'application/json',
    //   },
    // });
    // console.log('r1', r1);
    // const r2 = await JSON.parse(r1);
    // console.log('r2', r2);
    fetch('./db.json')
      .then(function (response) {
        return response.json();
      })
      .then(function (myJson) {
        console.log(myJson);
      })
      .finally(err => {
        err && console.log(err);
      });
  };

  useEffect(() => {
    fetchData();
    fetchData2();
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
