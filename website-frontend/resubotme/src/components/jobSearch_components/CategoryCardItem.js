import React from 'react'
import { Link } from 'react-router-dom'


function CategoryCardItem(props) {
  return (
    <>
        <li className='cards__item'>
            <Link className="cards__item__link" >


                <div className='cards__item__info'>
                    <h1 className='cards__item__categoryRank'>{props.rank}</h1>
                    <h3 className='cards__item__categoryTitle'>{props.title}</h3>
                    <h5 className='cards__item__categoryText'>{props.text}</h5>
                    

                </div>
                
                

            </Link>
        </li>


    </>
  )
}

export default CategoryCardItem
