msg_panel = document.getElementsByClassName("_33LGR")[0];
top = [];
while(top.length === 0){
    tentatives = 3;
    while(tentatives > 0){
        spinner = document.getElementsByClassName("PWkc7");
        if(spinner.length === 1){
            tentatives = 0;
        }
        else{
            await new Promise(r => setTimeout(r, 2000));
            tentatives-=1;
        }
    }
    msg_panel.scrollTo(0, 0);
    top = document.getElementsByClassName("cvjcv _1p8Qv EtBAv");
}


msg_panel = document.getElementsByClassName("_33LGR")[0];
top = [];
while(top.length === 0){
    tentatives = 3;
    while(tentatives > 0){
        spinner = document.getElementsByClassName("PWkc7");
        if(spinner.length === 0){
            tentatives = 0;
        }
        else{
            await new Promise(r => setTimeout(r, 5000))
            tentatives-=1;
        }
    }
    msg_panel.scrollTo(0, 0);
    await new Promise(r => setTimeout(r, 2000))
    top = document.getElementsByClassName("cvjcv _1p8Qv EtBAv");
}