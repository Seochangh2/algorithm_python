function solution(t, p) {
    var answer = 0;
    var N = t.length;

    for(var i=0;i<=N-p.length;i++){
        var tmp = t.substr(i,p.length);
        if(parseInt(p) >= parseInt(tmp)) answer += 1;
    }
    return answer;
}