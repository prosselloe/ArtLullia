var _____WB$wombat$assign$function_____=function(name){return (globalThis._wb_wombat && globalThis._wb_wombat.local_init && globalThis._wb_wombat.local_init(name))||globalThis[name];};if(!globalThis.__WB_pmw){globalThis.__WB_pmw=function(obj){this.__WB_source=obj;return this;}}{
let window = _____WB$wombat$assign$function_____("window");
let self = _____WB$wombat$assign$function_____("self");
let document = _____WB$wombat$assign$function_____("document");
let location = _____WB$wombat$assign$function_____("location");
let top = _____WB$wombat$assign$function_____("top");
let parent = _____WB$wombat$assign$function_____("parent");
let frames = _____WB$wombat$assign$function_____("frames");
let opener = _____WB$wombat$assign$function_____("opener");
var elem;
if(document.getElementsByTagName)
{
elem = document.body.getElementsByTagName("div");
}
for (var i = 0; i < elem.length; i++)
{
if(elem[i].style.display=='none') elem[i].style.display='';
}
var T=Math.random();
var Ref=document.referrer;
if (typeof(parent.document)!="unknown")
{
var F=parent.document.URL;
if (document.referrer==F) Ref=parent.document.referrer;
}
var S="usr="+AFS_Account+"P"+AFS_Tracker+"&js=1";
if (typeof AFS_Page == "undefined") var AFS_Page="unknown";
if (typeof AFS_Url == "undefined") var AFS_Url="unknown";
if (AFS_Page=="DetectName") {AFS_Page=document.title;}
if (AFS_Url=="DetectUrl") {AFS_Url=window.document.URL;}
S+="&title="+escape(AFS_Page);
S+="&url="+escape(AFS_Url);
S+="&refer="+escape(Ref);
if(typeof(screen)=="object")
{
S+="&resolution="+screen.width+"x"+screen.height;
S+="&color="+screen.colorDepth;
}
S+="&Tips="+T;
document.write("<a href='https://web.archive.org/web/20110707082858/http://new.addfreestats.com/?usr="+AFS_Account+"' >");
document.write("<img border=0 src='http://"+AFS_Server+".addfreestats.com/cgi-bin/connect.cgi?");
document.write(S);
document.write("' border=0 alt='' title='Free Web Stats'></a>");

}

/*
     FILE ARCHIVED ON 08:28:58 Jul 07, 2011 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 10:40:10 Jul 12, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  capture_cache.get: 0.498
  load_resource: 134.236
  PetaboxLoader3.resolve: 34.847
  PetaboxLoader3.datanode: 27.625
*/