var cur_selected = 0;

function song_select(clicked_id){
    if(clicked_id == "af1"){
        document.getElementById("audio").src = "https://p.scdn.co/mp3-preview/df8f112527e50dd51a36f0868a297faa7029fa8b?cid=0a3419c6f1934f9c85e6f0381335c2b0";
        cur_selected = 1;
    }
    else if(clicked_id == "af2"){
        document.getElementById("audio").src = "https://p.scdn.co/mp3-preview/82b805129e489c6410fbae3cd22937d5e5981b01?cid=0a3419c6f1934f9c85e6f0381335c2b0";
        cur_selected = 2;
    }
    else if(clicked_id == "af3"){
        document.getElementById("audio").src= "https://p.scdn.co/mp3-preview/b9aba60296e808a2c091ecdd7f374235dde70dc4?cid=0a3419c6f1934f9c85e6f0381335c2b0";
        cur_selected = 3;
    }
    return 0;
}