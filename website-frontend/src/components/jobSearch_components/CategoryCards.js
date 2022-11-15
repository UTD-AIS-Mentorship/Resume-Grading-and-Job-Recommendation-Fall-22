import React from 'react'
import CategoryCardItem from './CategoryCardItem'
import './CategoryCards.css';

function CategoryCards() {
  return (
    <div className='cards'>
        <h1> Title</h1>
        <div className='cards__container'>
            <div className='cards__wrapper'>
                <ul className='cards__items'>
                    <CategoryCardItem 
                        rank="1"
                        title="Filler"
                        text="Filler"
                    />
                    <CategoryCardItem 
                        rank="1"
                        title="Filler"
                        text="Filler"
                    />
                    <CategoryCardItem 
                        rank="1"
                        title="Filler"
                        text="Filler"
                    />
                </ul>
            </div>
        </div>
      
    </div>
  )
}

export default CategoryCards;