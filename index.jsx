import React, { useState, useEffect, useRef } from 'react';
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
  const originData = useRef(null);
  const [data, setData] = useState([]);
  const [count, setCount] = useState(0);
  const [catalogList, setCatalogList] = useState([]);
  const [searchValue, setSearchValue] = useState('');

  useEffect(() => {
    fetchData();
  }, [count]);

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
    originData.current = data;
  };
  const handelToggleDarkMode = () => {
    var element = document.body;
    element.classList.toggle('dark-mode');
  };
  const handelRefresh = () => {
    setCount(c => c + 1);
  };
  const handelInputChange = e => {
    e.preventDefault();
    const val = e.target.value;
    console.log('val', val);
    setSearchValue(val);
    if (val) {
      filterFetchData(String(val).toLowerCase());
    } else {
      handleResetSearchValue();
    }
  };
  const filterFetchData = str => {
    console.log('str', str);
    const filteredData = originData.current.filter(
      ({ value: { describe, describtion } }) =>
        (describe || describtion).toLowerCase().includes(str),
    );
    // console.log('filteredData', filteredData);
    setData(filteredData);
  };
  const handleResetSearchValue = () => {
    setSearchValue('');
    setData(originData.current);
  };
  if (!data.length && !originData) {
    return <Loading />;
  }
  return (
    <>
      <div
        className="container"
        style={{
          padding: '15px',
        }}
      >
        <div className="columns">
          <div
            className="column col-auto"
            style={{
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
            }}
          >
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
          <div className="column ">
            <div
              className="columns"
              style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
              }}
            >
              <div className="column col-auto">
                <input
                  className="form-input"
                  type="text"
                  value={searchValue}
                  style={{
                    // marginLeft: '20px',
                    width: '200px',
                    height: '28px',
                  }}
                  onChange={handelInputChange}
                  placeholder="search..."
                />
              </div>
              <div className="column">
                <button className="btn btn-sm" onClick={handleResetSearchValue}>
                  reset
                </button>
              </div>
            </div>
          </div>
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
