const state={resources:[],lang:"en"};
const $=s=>document.querySelector(s);
const translations={
 en:{
  eyebrow:"OPEN INTELLIGENCE ATLAS",title:"Find the right source for the evidence you actually have.",
  subtitle:"Search by jurisdiction, discipline, input, validation state and execution model. The page reads the same canonical catalogue used by CI.",
  resources:"resources",verified:"verified",jurisdictions:"jurisdictions",inputs:"input classes",search:"Search",
  searchPlaceholder:"Search name, domain, use case, discipline...",allJurisdictions:"All jurisdictions",allDisciplines:"All disciplines",
  allInputs:"All inputs",allStatuses:"All statuses",allExecution:"All execution classes",clear:"Clear filters",
  evidenceFirst:"Evidence first, automation second.",methodText:"A catalogue hit is a lead. AI output is not evidence. Entity similarity never auto-merges identities. Preserve source, capture time and provenance before drawing conclusions.",
  footer:"AI-assisted curation · human validation · lawful use",shown:n=>`${n} resources shown`,open:"Open resource",noResults:"No resources match these filters."
 },
 pt:{
  eyebrow:"ATLAS ABERTO DE INTELIGÊNCIA",title:"Encontre a fonte certa para a evidência que você realmente tem.",
  subtitle:"Pesquise por jurisdição, disciplina, tipo de entrada, validação e modelo de execução. A página usa o mesmo catálogo canônico validado pelo CI.",
  resources:"recursos",verified:"verificados",jurisdictions:"jurisdições",inputs:"tipos de entrada",search:"Pesquisar",
  searchPlaceholder:"Pesquise nome, domínio, caso de uso, disciplina...",allJurisdictions:"Todas as jurisdições",allDisciplines:"Todas as disciplinas",
  allInputs:"Todos os tipos de entrada",allStatuses:"Todos os status",allExecution:"Todos os modelos de execução",clear:"Limpar filtros",
  evidenceFirst:"Evidência primeiro, automação depois.",methodText:"Um resultado do catálogo é uma pista. Saída de IA não é evidência. Similaridade entre entidades nunca deve fundir identidades automaticamente. Preserve fonte, horário de captura e proveniência antes de concluir.",
  footer:"curadoria assistida por IA · validação humana · uso lícito",shown:n=>`${n} recursos exibidos`,open:"Abrir recurso",noResults:"Nenhum recurso corresponde a estes filtros."
 }
};
function tr(k){return translations[state.lang][k]??k}
function localize(){
 document.documentElement.lang=state.lang;
 document.querySelectorAll("[data-i18n]").forEach(el=>el.textContent=tr(el.dataset.i18n));
 document.querySelectorAll("[data-i18n-placeholder]").forEach(el=>el.placeholder=tr(el.dataset.i18nPlaceholder));
 $("#langBtn").textContent=state.lang==="en"?"PT":"EN";
 render();
}
function uniq(field){
 const s=new Set(); state.resources.forEach(r=>(r[field]||[]).forEach(v=>s.add(v))); return [...s].sort();
}
function fillSelect(id,values){
 const select=$(id); const keep=select.options[0]; select.replaceChildren(keep);
 values.forEach(v=>{const o=document.createElement("option");o.value=v;o.textContent=v;select.appendChild(o)});
}
function initFilters(){
 fillSelect("#jurisdiction",uniq("jurisdictions"));
 fillSelect("#discipline",uniq("disciplines"));
 fillSelect("#input",uniq("target_inputs"));
 fillSelect("#status",[...new Set(state.resources.map(r=>r.status))].sort());
 fillSelect("#execution",[...new Set(state.resources.map(r=>r.execution_class).filter(Boolean))].sort());
}
function params(){
 return {
  q:$("#q").value.trim().toLowerCase(),jurisdiction:$("#jurisdiction").value,
  discipline:$("#discipline").value,input:$("#input").value,status:$("#status").value,execution:$("#execution").value
 };
}
function matches(r,p){
 const hay=[r.name,r.id,r.notes,...(r.domains||[]),...(r.use_cases||[]),...(r.disciplines||[]),...(r.jurisdictions||[]),...(r.target_inputs||[])].filter(Boolean).join(" ").toLowerCase();
 return (!p.q||hay.includes(p.q))&&(!p.jurisdiction||(r.jurisdictions||[]).includes(p.jurisdiction))&&
 (!p.discipline||(r.disciplines||[]).includes(p.discipline))&&(!p.input||(r.target_inputs||[]).includes(p.input))&&
 (!p.status||r.status===p.status)&&(!p.execution||r.execution_class===p.execution);
}
function card(r){
 const el=document.createElement("article");el.className="card";el.id=r.id;
 const inputs=(r.target_inputs||[]).slice(0,4); const tags=[...(r.domains||[]).slice(0,3),...inputs.slice(0,2)];
 el.innerHTML=`
  <div class="card-head"><h2>${escapeHtml(r.name)}</h2><span class="status ${r.status}">${escapeHtml(r.status)}</span></div>
  <div class="meta">${escapeHtml((r.jurisdictions||[]).join(" · "))} · ${escapeHtml((r.disciplines||[]).join(" · "))} · ${escapeHtml(r.implementation_type||"resource")}</div>
  <div class="tags">${tags.map(x=>`<span class="tag">${escapeHtml(x)}</span>`).join("")}</div>
  <p class="notes">${escapeHtml(r.notes||((r.use_cases||[]).join(" · "))||"")}</p>
  <div class="card-actions"><a href="${encodeURI(r.canonical_url)}" target="_blank" rel="noopener noreferrer">${tr("open")} ↗</a><a class="permalink" href="#${encodeURIComponent(r.id)}" title="Permalink">#</a></div>`;
 return el;
}
function escapeHtml(v){return String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]))}
function updateUrl(p){
 const u=new URL(location.href);["q","jurisdiction","discipline","input","status","execution"].forEach(k=>p[k]?u.searchParams.set(k,p[k]):u.searchParams.delete(k));
 history.replaceState(null,"",u);
}
function render(){
 if(!state.resources.length)return;
 const p=params();updateUrl(p);
 const items=state.resources.filter(r=>matches(r,p)).sort((a,b)=>(a.status!=="verified")-(b.status!=="verified")||a.name.localeCompare(b.name));
 $("#resultCount").textContent=tr("shown")(items.length); const root=$("#results");root.innerHTML="";
 if(!items.length){root.innerHTML=`<div class="empty">${tr("noResults")}</div>`;return}
 items.forEach(r=>root.appendChild(card(r)));
}
function restoreParams(){
 const p=new URLSearchParams(location.search);
 ["q","jurisdiction","discipline","input","status","execution"].forEach(k=>{const el=$("#"+k);if(el&&p.has(k))el.value=p.get(k)});
}
async function boot(){
 const res=await fetch("./data/resources.json",{cache:"no-store"});const payload=await res.json();state.resources=payload.resources||[];
 initFilters();restoreParams();
 $("#statTotal").textContent=state.resources.length;
 $("#statVerified").textContent=state.resources.filter(r=>r.status==="verified").length;
 $("#statJurisdictions").textContent=new Set(state.resources.flatMap(r=>r.jurisdictions||[])).size;
 $("#statInputs").textContent=new Set(state.resources.flatMap(r=>r.target_inputs||[])).size;
 ["#q","#jurisdiction","#discipline","#input","#status","#execution"].forEach(s=>$(s).addEventListener("input",render));
 $("#clearBtn").addEventListener("click",()=>{["#q","#jurisdiction","#discipline","#input","#status","#execution"].forEach(s=>$(s).value="");render()});
 $("#langBtn").addEventListener("click",()=>{state.lang=state.lang==="en"?"pt":"en";localize()});
 localize();
 if(location.hash){setTimeout(()=>document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView({block:"center"}),50)}
}
boot().catch(err=>{$("#results").innerHTML=`<div class="empty">Catalogue load failed: ${escapeHtml(err.message)}</div>`});
