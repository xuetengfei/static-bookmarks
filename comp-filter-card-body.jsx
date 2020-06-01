import React from 'react';

const Component = props => {
  const { data, catalogList } = props;
  return (
    <>
      <div className="filter-body columns col-gapless">
        {data.map(({ id, value }) => (
          <div
            className="column col-3 filter-item"
            data-tag={`tag-${
              catalogList.find(v => v.name === value.catalog).idx
            }`}
            key={id}
          >
            <div className="card">
              <div className="card-header">
                <div className="card-title text-bold">
                  <a href={value.url} target="_blank">
                    {value.describe || value.describtion}
                  </a>
                  <sub className="book-mark-item-id">{id}</sub>
                </div>
                {/* <div className="card-subtitle text-gray">{id}</div> */}
              </div>
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default Component;
