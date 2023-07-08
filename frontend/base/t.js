let a = ({ b }) => {
    console.log({ b: 'hi' });
    console.log(typeof b);
    console.log(b);
    console.log("hi");
};

let b = 0;
a({b:1});

// let a = (b) => {};
// let a = ({ b }) => {};
