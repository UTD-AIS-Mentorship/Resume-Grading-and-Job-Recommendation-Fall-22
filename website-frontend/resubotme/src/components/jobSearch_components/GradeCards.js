import React from 'react'
import GradeCardItem from './GradeCardItem'
import './CategoryCards.css';

function GradeCards() {
  return (
    <div className='cards'>
        <h1> Title</h1>
        <div className='cards__container'>
            <div className='cards__wrapper'>
                <ul className='cards__items'>
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                    <GradeCardItem 
                        
                        title="Filler"
                        desc="Filler"
                        percent= { 90 }
                    />
                </ul>
            </div>
        </div>
      
    </div>
  )
}

export default GradeCards;