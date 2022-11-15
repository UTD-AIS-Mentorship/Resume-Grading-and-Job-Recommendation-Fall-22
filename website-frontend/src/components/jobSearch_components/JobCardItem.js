import React from 'react'
import { Link } from 'react-router-dom'
import RadialBar from '../other_components/RadialBar'

import VisibilitySensor from "react-visibility-sensor";

function JobCardItem(props) {
  return (
    <>
        <li className='cards__item'>
            

                <figure className="cards__item__pic-wrap" data-category={props.label}>
                    <img src="/" alt="Backup" className="cards__item__img" />
                </figure>

                <div className='cards__item__info'>
                    <h3 className='cards__item__jobTitle'>{props.text}</h3>
                    <h5 className='cards__item__jobCompany'>Job Company</h5>
                    <h5 className='cards__item__jobLocation'>Job Location</h5>

                    <div style={{ width: 200, height: 200 }}>
                        <VisibilitySensor>
                            {({ isVisible }) => {
                            const percentage = isVisible ? props.percent : 0;
                            return (
                                <RadialBar value={percentage} number={percentage} />
                            );
                            }}
                        </VisibilitySensor>
                    </div>
                    <Link className="cards__item__link" >
                        <button className='cards__item__btn' to={props.path}> APPLY </button>
                    </Link>
                </div>
                
                

        </li>


    </>
  )
}

export default JobCardItem