import React from 'react';

const Item = props => {
  const { value, id } = props;

  const elementProps = {};
  if (value.detail) {
    elementProps['data-tooltip'] = value.detail;
    elementProps['className'] = 'tooltip';
  }
  return (
    <div {...elementProps}>
      <a href={value.url} target="_blank">
        {value.describe || value.describtion}
      </a>
      <sub className="book-mark-item-id">{id}</sub>
    </div>
  );
};

const Component = props => {
  const { data, catalogList } = props;
  return (
    <>
      <div className="filter-body columns col-gapless">
        {data.map(({ id, value }) => (
          <div
            className="column col-xs-12 col-sm-12 col-lg-4 col-xl-3 col-3 filter-item"
            data-tag={`tag-${
              catalogList.find(v => v.name === value.catalog).idx
            }`}
            key={id}
          >
            <div className="card">
              <div className="card-header">
                <div className="card-title text-bold">
                  <Item id={id} value={value} />
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Component;
