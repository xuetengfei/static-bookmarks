import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import 'babel-polyfill';
import 'spectre.css';
import ToggleButton from './comp-toggle-button';
import FilterCard from './comp-filter-card-body';
import ErrorBoundary from './comp-error-boundary';
import './_filters.scss';
import './custom.scss';

const api =
  'https://raw.githubusercontent.com/xuetengfei/my_json_data/master/book_marks.json';

const App = () => {
  const [data, setData] = useState([]);
  const [catalogList, setCatalogList] = useState([]);

  const fetchData = async () => {
    const res = await fetch(api);
    const { all } = await res.json();
    const data = Object.entries(all).map(([key, value]) => ({
      id: key,
      value,
    }));
    const catalogList = data
      .map(v => v.value.catalog)
      .filter((el, idx, arr) => idx === arr.indexOf(el));
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
  return (
    <>
      <div
        className="divider text-center"
        data-content="xuetengfei's bookMarks"
      ></div>
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
<br />;

ReactDOM.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
  document.getElementById('root'),
);
