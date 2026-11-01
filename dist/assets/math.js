// Pure, dependency-free calculation functions. UI and tests use this same module.
export function number(v, label, min=0, max=100) {
  if (v === null || v === undefined || String(v).trim()==='') throw new Error(`${label} is required.`);
  const n=Number(v);
  if (!Number.isFinite(n) || n<min || n>max) throw new Error(`${label} must be between ${min} and ${max}.`);
  return n;
}
export function finalNeeded(current,target,weight){
  const c=number(current,'Current grade'),t=number(target,'Target grade'),w=number(weight,'Final weight',0.01,100)/100;
  return (t-c*(1-w))/w;
}
export function finalOverall(current,exam,weight){
  const c=number(current,'Current grade'),e=number(exam,'Exam score'),w=number(weight,'Final weight',0.01,100)/100;
  return c*(1-w)+e*w;
}
export function weighted(rows,mode='percent'){
  if (!rows.length) throw new Error('Add at least one completed assessment.');
  let sum=0,total=0;
  for(const [i,row] of rows.entries()){
    const s=number(row[0],`Score in row ${i+1}`),w=number(row[1],`Weight in row ${i+1}`,0.000001,10000);
    sum+=s*w;total+=w;
  }
  if(mode==='percent' && total>100+1e-8) throw new Error('Percentage weights cannot total more than 100%.');
  return {average:sum/total,weight:total,contribution:sum/100,remaining:Math.max(0,100-total)};
}
export function gpa(rows,max=4){
  const scale=number(max,'Scale',1,10);
  if(!rows.length)throw new Error('Add at least one GPA-bearing course.');
  let points=0,credits=0;
  rows.forEach(([g,c],i)=>{const grade=number(g,`Grade points in row ${i+1}`,0,scale),credit=number(c,`Credits in row ${i+1}`,0.000001,10000);points+=grade*credit;credits+=credit;});
  return {value:points/credits,points,credits};
}
export function cumulative(oldGpa,oldCredits,newGpa,newCredits,max=4){
  return gpa([[oldGpa,oldCredits],[newGpa,newCredits]],max);
}
export function percentage(earned,possible){
  const p=number(possible,'Possible points',0.000001,1000000),e=number(earned,'Earned points',0,p);
  return e/p*100;
}
export function testScore(total,wrong){
  const t=number(total,'Total questions',1,1000000),w=number(wrong,'Incorrect answers',0,t);
  if(!Number.isInteger(t)||!Number.isInteger(w))throw new Error('Question counts must be whole numbers.');
  return {correct:t-w,percent:(t-w)/t*100};
}
export function average(values){
  if(!values.length)throw new Error('Enter at least one grade.');
  const v=values.map((x,i)=>number(x,`Grade ${i+1}`));
  return {value:v.reduce((a,b)=>a+b,0)/v.length,count:v.length,min:Math.min(...v),max:Math.max(...v)};
}
export function minimumDisplayed(value){return Math.ceil((value-1e-10)*100)/100;}
