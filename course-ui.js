/* Shared course shell: rail, dashboard and weekly module hero. */
(function(){
  "use strict";
  var DATA = window.COURSE_DATA;
  if(!DATA || !DATA.phases) return;
  var path = location.pathname;
  var isTracker = /metabolic-engineering-tracker\.html$/.test(path);
  var inLecture = /\/lecture-notes\//.test(path);
  var base = inLecture ? "../" : "";
  var weekMatch = path.match(/week-(\d+)\.html$/);
  var current = weekMatch ? parseInt(weekMatch[1],10) : 0;
  var state = {};
  try{ state = JSON.parse(localStorage.getItem("me55.v1")||"{}") || {}; }catch(e){ state = {}; }
  var done = state.done || {};
  var DL = DATA.weeks;
  function phaseOf(n){ for(var i=0;i<DATA.phases.length;i++){var p=DATA.phases[i]; if(n>=p.weeks[0]&&n<=p.weeks[1]) return p;} return DATA.phases[0]; }
  function weekDone(n){ var c=0; for(var i=1;i<=12;i++) if(done[n+"-"+i]) c++; return c; }
  function activeWeek(){ for(var n=1;n<=DL.length;n++) if(weekDone(n)<12) return n; return DL.length; }
  if(!current && isTracker) current = activeWeek();
  document.body.classList.add("course-shell", isTracker ? "tracker-shell" : "module-shell");

  /* Rail */
  var rail = document.createElement("aside");
  rail.className = "course-rail"; rail.id = "courseRail"; rail.setAttribute("aria-label","Course modules");
  var brand = document.createElement("a"); brand.className="rail-brand"; brand.href=base+"index.html";
  brand.innerHTML = '<span class="rail-logo">ME</span><span><b>Metabolic Engineering</b><span>55 weeks · 660 sessions</span></span>';
  rail.appendChild(brand);
  var scroll = document.createElement("div"); scroll.className="rail-scroll";
  var dash = document.createElement("a"); dash.className="rail-link"; dash.href=base+"metabolic-engineering-tracker.html";
  dash.innerHTML='<span class="ri">◫</span>Dashboard'; scroll.appendChild(dash);
  var sh = document.createElement("a"); sh.className="rail-link"; sh.href=base+"start-here.html";
  sh.innerHTML='<span class="ri">◎</span>Start here'; scroll.appendChild(sh);
  var lab = document.createElement("div"); lab.className="rail-label"; lab.textContent="Modules"; scroll.appendChild(lab);
  DATA.phases.forEach(function(p){
    var d=document.createElement("details"); d.className="rail-module"; d.dataset.phase=p.id;
    var isCur = current>=p.weeks[0] && current<=p.weeks[1]; if(isCur) d.open=true;
    var sm=document.createElement("summary");
    sm.innerHTML='<span class="rail-dot"></span><span>'+p.name+'</span><span class="rmeta">'+p.weeks[0]+'–'+p.weeks[1]+'</span>';
    d.appendChild(sm);
    var list=document.createElement("div"); list.className="rail-weeks";
    for(var n=p.weeks[0];n<=p.weeks[1];n++){
      var w=DL[n-1]; if(!w) continue;
      var a=document.createElement("a"); a.className="rail-week"; a.href=base+"lecture-notes/week-"+String(n).padStart(2,"0")+".html";
      if(n===current) a.classList.add("current");
      if(weekDone(n)===12) a.classList.add("done");
      a.innerHTML='<span class="rn">'+n+'</span><span>'+w.t+'</span>';
      a.title="Week "+n+": "+w.t; list.appendChild(a);
    }
    d.appendChild(list); scroll.appendChild(d);
  });
  rail.appendChild(scroll);
  var saved=document.createElement("div"); saved.className="rail-saved"; saved.innerHTML='<i></i>Saved in this browser'; rail.appendChild(saved);
  var scrim=document.createElement("div"); scrim.className="rail-scrim"; scrim.id="railScrim";
  var toggle=document.createElement("button"); toggle.className="course-rail-toggle"; toggle.type="button"; toggle.id="railToggle"; toggle.setAttribute("aria-controls","courseRail"); toggle.setAttribute("aria-expanded","false"); toggle.textContent="☰ Modules";
  document.body.insertBefore(rail, document.body.firstChild); document.body.appendChild(scrim); document.body.appendChild(toggle);
  function closeRail(){ rail.classList.remove("open"); scrim.classList.remove("open"); toggle.setAttribute("aria-expanded","false"); }
  toggle.addEventListener("click",function(){ var open=rail.classList.toggle("open"); scrim.classList.toggle("open",open); toggle.setAttribute("aria-expanded",String(open)); });
  scrim.addEventListener("click",closeRail);
  rail.querySelectorAll("a").forEach(function(a){a.addEventListener("click",closeRail);});

  /* Dashboard cards on tracker */
  if(isTracker){
    var mast=document.querySelector(".mast");
    if(mast){
      mast.classList.add("dash-mast");
      if(!mast.querySelector(".welcome-kicker")){
        var wk=document.createElement("p"); wk.className="welcome-kicker"; wk.textContent="Welcome back"; mast.insertBefore(wk,mast.firstChild);
      }
      var tabs=document.querySelector("nav.tabs");
      var sec=document.createElement("section"); sec.className="course-dashboard"; sec.setAttribute("aria-label","Course content");
      var top=document.createElement("div"); top.className="dash-top"; top.innerHTML='<h2>Course content</h2><span>8 modules · 55 weeks · 660 sessions</span>';
      var grid=document.createElement("div"); grid.className="phase-grid";
      DATA.phases.forEach(function(p){
        var total=(p.weeks[1]-p.weeks[0]+1)*12; var doneN=0;
        for(var n=p.weeks[0];n<=p.weeks[1];n++) doneN+=weekDone(n);
        var pct=Math.round(100*doneN/total);
        var a=document.createElement("a"); a.className="phase-card p"+p.id; a.href=base+"lecture-notes/week-"+String(p.weeks[0]).padStart(2,"0")+".html";
        var status=doneN===total?"Complete":doneN>0?"In progress":(current>=p.weeks[0]&&current<=p.weeks[1]?"In progress":"Upcoming");
        a.innerHTML='<div class="phase-band">Module '+p.id+' · Wk '+p.weeks[0]+'–'+p.weeks[1]+'</div><div class="phase-body"><h3>'+p.name+'</h3><p>'+(p.weeks[1]-p.weeks[0]+1)+' weeks · '+total+' sessions</p><div class="phase-bar"><i style="width:'+pct+'%"></i></div><div class="phase-foot"><span class="phase-pill">'+status+'</span><span>'+pct+'%</span></div></div>';
        grid.appendChild(a);
      });
      sec.appendChild(top); sec.appendChild(grid);
      if(tabs && tabs.parentNode) tabs.parentNode.insertBefore(sec,tabs); else mast.after(sec);
    }
  }

  /* Weekly module hero and plan */
  if(weekMatch && !isTracker){
    var w=DL[current-1]; if(!w) return;
    var p=phaseOf(current); var wrap=document.querySelector("main.wrap"); if(!wrap) return;
    var kicker=wrap.querySelector(".doc-kicker"); var h1=wrap.querySelector("h1");
    if(!kicker || !h1) return;
    var hero=document.createElement("section"); hero.className="module-hero"; hero.dataset.phase=p.id;
    var count=weekDone(current);
    hero.innerHTML='<div class="hero-actions"><a class="hero-btn" id="startModule" href="#moduleBody">▶ Start module</a><a class="hero-btn ghost" href="'+base+'CASE-THREAD.md">Case thread</a><div class="hero-progress">'+count+' / 12 sessions complete<div class="bar"><i style="width:'+Math.round(count/12*100)+'%"></i></div></div></div>';
    kicker.replaceWith(hero); hero.insertBefore(kicker,hero.firstChild); hero.insertBefore(h1,kicker.nextSibling);
    var sub=document.createElement("p"); sub.className="hero-sub"; sub.textContent=(p.goal?p.goal.split(". ")[0]+".":"Week "+current+" of 55.");
    hero.insertBefore(sub,h1.nextSibling);
    // plan
    var plan=document.createElement("section"); plan.className="module-plan"; plan.setAttribute("aria-label","Week plan");
    var obj=document.createElement("div"); obj.className="module-objectives";
    (w.obj||[]).forEach(function(o){ var li=document.createElement("li"); li.textContent=o; obj.appendChild(li); });
    plan.innerHTML='<h2>Learning objectives</h2>';
    var ul=document.createElement("ul"); ul.className="module-objectives"; Array.from(obj.children).forEach(function(li){ul.appendChild(li);});
    plan.appendChild(ul);
    var det=document.createElement("details"); det.open=true; det.innerHTML='<summary>Week plan · 12 sessions</summary>';
    var ol=document.createElement("ol"); ol.className="session-list";
    (w.s||[]).forEach(function(t,i){var li=document.createElement("li");li.className="session-row";li.innerHTML='<b>'+(i+1)+'</b><span>'+t+'</span>';ol.appendChild(li);});
    det.appendChild(ol); plan.appendChild(det); hero.after(plan);
    var body=document.createElement("div"); body.className="module-body"; body.id="moduleBody";
    var node=plan.nextSibling; while(node){var next=node.nextSibling; body.appendChild(node); node=next;}
    wrap.appendChild(body);
    var foot=document.createElement("div"); foot.className="module-footnav";
    var prev=current>1?'<a href="week-'+String(current-1).padStart(2,"0")+'.html">← Week '+(current-1)+'</a>':'<a href="index.html">← Lecture index</a>';
    var next=current<55?'<a href="week-'+String(current+1).padStart(2,"0")+'.html">Week '+(current+1)+' →</a>':'<a href="../metabolic-engineering-tracker.html">Course tracker →</a>';
    foot.innerHTML=prev+next; wrap.appendChild(foot);
    var start=document.getElementById("startModule"); if(start) start.addEventListener("click",function(e){ e.preventDefault(); body.scrollIntoView({behavior:"smooth",block:"start"}); });
  }
})();
