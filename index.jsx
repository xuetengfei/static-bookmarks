import React, { useState, useEffect, useRef, useCallback } from 'react';
import ReactDOM from 'react-dom';
import { inject } from '@vercel/analytics';
import 'spectre.css';
import ToggleButton from './comp-toggle-button';
import FilterCard from './comp-filter-card-body';
import ErrorBoundary from './comp-error-boundary';
import 'babel-polyfill';
import './_filters.scss';
import './_custom.scss';
import './custom.css';

// 加载组件
const Loading = () => <div className="loading loading-lg loading-position" />;

const App = () => {
  // 使用 useRef 存储原始数据
  const originData = useRef(null);
  // 使用 useState 管理状态
  const [data, setData] = useState([]);
  const [count, setCount] = useState(0);
  const [catalogList, setCatalogList] = useState([]);
  const [searchValue, setSearchValue] = useState('');

  // 获取数据的函数
  const fetchData = useCallback(async () => {
    try {
      const response = await fetch('./db.json');
      const DB = await response.json();
      const { all } = DB;

      // 处理数据
      const processedData = Object.entries(all)
        .map(([key, value]) => ({ id: key, value }))
        .sort((a, b) => Number(b.id) - Number(a.id));

      // 提取目录列表
      const uniqueCatalogs = [
        ...new Set(processedData.map(v => v.value.catalog)),
      ].sort();

      // 设置目录列表
      setCatalogList([
        { name: 'all', idx: 0 },
        ...uniqueCatalogs.map((name, idx) => ({ name, idx: idx + 1 })),
      ]);

      // 更新数据状态
      setData(processedData);
      originData.current = processedData;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }, []);

  // 使用 useEffect 在组件挂载和 count 变化时获取数据
  useEffect(() => {
    fetchData();
    inject();
  }, [count, fetchData]);

  // 切换暗黑模式
  const handleToggleDarkMode = () => {
    document.body.classList.toggle('dark-mode');
  };

  // 刷新数据
  const handleRefresh = () => setCount(c => c + 1);

  // 处理搜索输入
  const handleInputChange = useCallback(e => {
    const val = e.target.value.toLowerCase();
    setSearchValue(val);

    if (val) {
      filterData(val);
    } else {
      handleResetSearchValue();
    }
  }, []);

  // 过滤数据
  const filterData = useCallback(str => {
    const filteredData = originData.current.filter(({ value }) => {
      const { describe, describtion, detail, url } = value;
      return (
        (describe || describtion || '').toLowerCase().includes(str) ||
        (detail || '').toLowerCase().includes(str) ||
        (url || '').toLowerCase().includes(str)
      );
    });
    setData(filteredData);
  }, []);

  // 重置搜索
  const handleResetSearchValue = useCallback(() => {
    setSearchValue('');
    setData(originData.current);
  }, []);

  // 如果没有数据，显示加载组件
  if (!data.length && !originData.current) {
    return <Loading />;
  }

  return (
    <>
      <div className="container" style={{ padding: '15px' }}>
        {/* 控制按钮 */}
        <div className="columns">
          <div className="column col-auto d-flex justify-content-center align-items-center">
            <button className="btn btn-sm mr-2" onClick={handleToggleDarkMode}>
              Toggle Mode
            </button>
            <button className="btn btn-sm" onClick={handleRefresh}>
              Refresh
            </button>
          </div>
          {/* 搜索输入 */}
          <div className="column">
            <div className="columns d-flex justify-content-center align-items-center">
              <div className="column col-auto">
                <input
                  className="form-input"
                  type="text"
                  value={searchValue}
                  style={{ width: '200px', height: '28px' }}
                  onChange={handleInputChange}
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
      {/* 过滤器和卡片 */}
      <div className="column col-12">
        <div className="filter">
          <ToggleButton catalogList={catalogList} />
          <div className="divider-space" />
          <FilterCard data={data} catalogList={catalogList} />
        </div>
      </div>
    </>
  );
};

// 渲染应用
ReactDOM.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
  document.getElementById('root'),
);
