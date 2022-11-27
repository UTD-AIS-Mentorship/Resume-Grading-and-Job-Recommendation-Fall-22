const robot = document.getElementById("Robot");

let prev = 0;
let mainInterval;
let combination = 0;

const startInterval = () => {
    mainInterval = setInterval(() => {
        combination = combination === 4? 0 : combination+1;
        robot.dataset.configuration = combination;
        prev = index;
        }, 1000);
}

const stopInterval = () => {
    clearInterval(mainInterval);
}

startInterval();

robot.addEventListener("click", clickToggle)
document.addEventListener('mousemove', (e)=> {
    const mouseX =e.clientX;
    const mouseY =e.clientY;
    const anchor = document.getElementById("Eyes");
    const rekt = anchor.getBoundingClientRect();
    const anchorX = rekt.left + rekt.width / 2;
    const anchorY = rekt.top + rekt.height / 2;
    const angleDeg = angle(mouseX, mouseY, anchorX, anchorY);
    const moveX = -5*Math.cos(angleDeg);
    const moveY = -5*Math.sin(angleDeg);
    anchor.style.transform = `translateY(${moveY}%) translateX(${moveX}%)`;
})

function angle(cx, cy, ex, ey) {
    const dy = ey - cy;
    const dx = ex - cx;
    const rad = Math.atan2(dy, dx);
    return rad;
}

function clickToggle() {
    robot.dataset.click = robot.dataset.click === 1? 0 : 1;
    console.log(robot.dataset.click)
}