import React from 'react'
//import { Link } from 'react-router-dom'
//import RadialBar from '../other_components/RadialBar'
import { CircularProgressbar } from 'react-circular-progressbar';
import "react-circular-progressbar/dist/styles.css"
import VisibilitySensor from "react-visibility-sensor";
import { NavLink } from "react-router-dom";

function JobCardItem(props) {
    const openInNewTab = url => {
        window.open(url, '_blank', 'noopener,noreferrer');
      };
  return (
    <>
            <div className="jobCards__item__link" >
                <div className='jobCards__item__bottom'>
                <a href={props.path} target="_blank" rel="noopener noreferrer">
                        <button className='jobCards__item__btn'  > APPLY </button>
                </a>

                
                    
                </div> 
                <div className="jobCards__item__left">
                    <h3 className='cards__item__jobTitle'>{props.text}</h3>
                    <h5 className='cards__item__jobCompany'>{props.company}</h5>
                    <h5 className='cards__item__jobLocation'>{props.location}</h5>
                </div>  
                <div className="jobCards__item__right">

                    <div className="jobCards__radial__chart" >
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
               
            </div>
    </>
  )
}

export default JobCardItem