import React from 'react'
import { Link } from 'react-router-dom'
import RadialBar from '../other_components/RadialBar'

import VisibilitySensor from "react-visibility-sensor"

function GradeCardItem(props) {
  return (
    <>
        <li className='cards__item'>
            <Link className="cards__item__link" >


                <div className='cards__item__info'>
                    <h3 className='cards__item__gradeTitle'>{props.title}</h3>
                    
                    <div style={{ width: 100, height: 100 }}>
                        <VisibilitySensor>
                            {({ isVisible }) => {
                            const percentage = isVisible ? props.percent : 0;
                            return (
                                <RadialBar value={percentage} number={percentage} />
                            );
                            }}
                        </VisibilitySensor>
                    </div>

                    <h5 className='cards__item__gradeDesc'>{props.desc}</h5>

                </div>
                
                

            </Link>
        </li>


    </>
  )
}

export default GradeCardItem