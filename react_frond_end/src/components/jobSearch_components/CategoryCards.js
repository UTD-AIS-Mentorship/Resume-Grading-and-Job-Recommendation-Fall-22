import React from 'react'
import CategoryCardItem from './CategoryCardItem'
import './CategoryCards.css';


function CategoryCards(data) {
    //<div className='cards__container'><div className='cards__wrapper'><JobCardItem text={value["positionName"]} company={value["company"]} location="Job Location" path={value["url"]} percent={value["similarity_score"]}/></div></div>
  return (
    <>
        <div className='cards__container'>
            <div className='cards__wrapper'>
                {
                    
                    data['catInfo'].map( (value) => ( 
                    <CategoryCardItem  
                    title={value[0]} 
                    percent={value[1]}/>
                    ))   
                }
                
                    
                    
                
            </div>
        </div>
      
    </>
  )
}

export default CategoryCards;