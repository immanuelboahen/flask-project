if (self.CavalryLogger) { CavalryLogger.start_js(["\/cWGl"]); }

__d('CrossWindowEventEmitter',['CacheStorage','EventEmitter'],(function a(b,c,d,e,f,g){'use strict';var h,i;h=babelHelpers.inherits(j,c('EventEmitter'));i=h&&h.prototype;function j(k){i.constructor.call(this);this.$CrossWindowEventEmitter2=k;this.$CrossWindowEventEmitter1=new (c('CacheStorage'))('localstorage',k+':');this.$CrossWindowEventEmitter1.addValueChangeCallback(function(l,m,n){var o,event=l.split(':')[1],p=n.__v;(o=i.emit).call.apply(o,[this,event].concat(p));}.bind(this));}j.prototype.emit=function(k){var l;for(var m=arguments.length,n=Array(m>1?m-1:0),o=1;o<m;o++)n[o-1]=arguments[o];this.emitRemote.apply(this,[k].concat(n));(l=i.emit).call.apply(l,[this,k].concat(n));};j.prototype.emitRemote=function(k){for(var l=arguments.length,m=Array(l>1?l-1:0),n=1;n<l;n++)m[n-1]=arguments[n];this.$CrossWindowEventEmitter1.set(k,m);};f.exports=j;}),null);