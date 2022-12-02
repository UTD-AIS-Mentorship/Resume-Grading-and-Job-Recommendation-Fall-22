import React from 'react'
import GradeCardItem from './GradeCardItem'
import './GradeCards.css';

function GradeCards(data) {
  return (
    <div>
        <div className='cards__container'>
            <div className='cards__wrapper'>
                    
                    {
                        Object.keys(data['gradesInfo']).map((key, index) => (<GradeCardItem title={key} desc={data['gradesInfo'][key]["Description"]} percent= {Math.round(data['gradesInfo'][key]["Score"] * 100)}/> ))
                        
                    }
            </div>
        </div>
      
    </div>
  )
}

export default GradeCards;