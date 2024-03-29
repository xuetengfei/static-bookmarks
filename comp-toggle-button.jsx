import React from 'react';

const Component = props => {
  const { catalogList } = props;
  return (
    <>
      {catalogList.map(({ name, idx }) => (
        <input
          className="filter-tag"
          id={`tag-${idx}`}
          key={idx}
          type="radio"
          name="filter-radio"
          hidden
        />
      ))}
      <div className="filter-nav">
        {catalogList.map(({ name, idx }) => (
          <label
            className="chip"
            htmlFor={`tag-${idx}`}
            key={idx}
            defaultChecked={idx === 10}
          >
            {name}
          </label>
        ))}
      </div>
    </>
  );
};

export default Component;
