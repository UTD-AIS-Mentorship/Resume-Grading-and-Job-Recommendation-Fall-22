import React from 'react'
import { Link } from 'react-router-dom'
import { CircularProgressbar } from 'react-circular-progressbar';
import "react-circular-progressbar/dist/styles.css"
import VisibilitySensor from "react-visibility-sensor";


function CategoryCardItem(props) {
  return (
    <>
        <li className='cards__item'>
            <Link className="cards__item__link" >


                <div className='cards__item__info'>
                  <div className='catCards_left'>
                    <h3 className='catCards__item__categoryTitle'>{props.title}</h3>
                    <h5 className='catCards__item__categoryText'>{props.text}</h5>
                  </div> 
                  <div className='catCards_right'>
                    <VisibilitySensor>
                        {({ isVisible }) => {
                        const percentage = isVisible ? props.percent : 0;
                        return (
                          <CircularProgressbar value={percentage} text={`${percentage}%`}/>
                        );
                        }}
                      </VisibilitySensor>
                    
                  </div> 

                </div>
                
                

            </Link>
        </li>


    </>
  )
}

export default CategoryCardItem
