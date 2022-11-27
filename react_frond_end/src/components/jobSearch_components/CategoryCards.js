import React from 'react'
import CategoryCardItem from './CategoryCardItem'
import './CategoryCards.css';

function CategoryCards() {
  return (
    <>
        <div className='cards__container'>
            <div className='cards__wrapper'>
                
                    <CategoryCardItem 
                        rank="1"
                        title="Filler"
                        text="Filler"
                    />
                    <CategoryCardItem 
                        rank="2"
                        title="Filler"
                        text="Filler"
                    />
                    <CategoryCardItem 
                        rank="3"
                        title="Filler"
                        text="Filler"
                    />
                
            </div>
        </div>
      
    </>
  )
}

export default CategoryCards;