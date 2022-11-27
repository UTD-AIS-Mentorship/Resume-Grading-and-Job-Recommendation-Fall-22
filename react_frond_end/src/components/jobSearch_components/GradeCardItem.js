import React from 'react'

//import RadialBar from '../other_components/RadialBar'
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar'
import "react-circular-progressbar/dist/styles.css"


import VisibilitySensor from "react-visibility-sensor"

function GradeCardItem(props) {
  return (
    <>
        
            <div className="cards__item__link" >


                <div className='cards__item__info'>
                    <div id="splitLeft">
                        <h3 className='gradeCards__item__gradeTitle'>{props.title}</h3>
                        <h5 className='gradeCards__item__gradeDesc' >{props.desc}</h5>

                    </div>
                    
                    
                    <div id="splitRight" >
                        <VisibilitySensor>
                                {({ isVisible }) => {
                                const percentage = isVisible ? props.percent : 0;
                                return (
                                    <CircularProgressbar value={percentage} 
                                    text={`${percentage}%`} 
                                    styles={buildStyles({
                                        textColor: "#e0e2db",
                                        pathColor: "#e6af2e",
                                        trailColor: "#e0e2db"
                                      })}/>
                                );
                                }}
                        </VisibilitySensor>
                    </div>
                </div>
            </div>
        


    </>
  )
}

export default GradeCardItem