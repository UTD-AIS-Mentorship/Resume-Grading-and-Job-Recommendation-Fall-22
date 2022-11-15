import React from "react";
//import {render} from "react-dom";
//import VisibilitySensor from "react-visibility-sensor";
import  {CircularProgressbar}  from 'react-circular-progressbar';


function RadialBar (props) {
    return (
        <div>   
            
            <CircularProgressbar
                percentage={props.percentage}
                text={
                    <tspan  dx={true? -15 : 0} dy={true? -15 : 0}>{props.number}%</tspan>
                }

                maxValue = {100}
                
                strokeWidth={5}
                
                styles={{
                    
                    root: {},
                    
                    path: {
                        stroke: '#f88',
                        strokeLinecap: 'butt',
                        transition: 'stroke-dashoffset 0.5s ease 0s',
                    },
                    
                    trail: {
                        stroke: '#d6d6d6',
                    },
                    
                    text: {
                        fill: '#f88',
                        fontSize: '30px',
                        
                    },
                }}
            />
        </div>

    );

}

export default RadialBar;