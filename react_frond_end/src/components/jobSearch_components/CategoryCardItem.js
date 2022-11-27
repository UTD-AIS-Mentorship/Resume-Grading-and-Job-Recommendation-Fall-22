import React from 'react'
import { Link } from 'react-router-dom'


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
                    <div className='rank_square'>
                      <h1 className='catCards__item__categoryRank'>{props.rank}</h1>
                    </div>
                  </div> 

                </div>
                
                

            </Link>
        </li>


    </>
  )
}

export default CategoryCardItem
