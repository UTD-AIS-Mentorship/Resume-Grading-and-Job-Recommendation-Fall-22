import React from 'react'
import JobCardItem from './JobCardItem'
import './JobCards.css';

function jobCards() {
  return (
    <div className='cards'>
        <h1> Title</h1>
        <div className='cards__container'>
            <div className='cards__wrapper'>
                <ul className='cards__items'>
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                    <JobCardItem 
                        text="Sample Text"
                        path=''
                        percent= { 90 }
                    />
                </ul>
            </div>
        </div>
      
    </div>
  )
}

export default jobCards;