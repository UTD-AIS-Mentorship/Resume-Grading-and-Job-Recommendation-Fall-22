import React from 'react';
import '../../App.css';
import {Button} from '../other_components/Button';
import './HeroSection.css';

function HeroSection() {
  return (
    <div className='hero-container'>
      <h1> resubot.me</h1>
      <div className = 'hero-btns'>
        <Button className='btns' buttonStyle='btn--outline' buttonSize='btn--large'>
            Get Started
        </Button>
      </div>    
    </div>
  )
}

export default HeroSection;
