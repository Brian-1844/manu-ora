# Patch "l'abeille ne suit le manu que quand le miel est prêt" — base v91 ou plus.
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    rep("bee=!!(garden.hive && garden.hive.seen && hiveFlowers().length>=2);","bee=!!(garden.hive && garden.hive.seen && garden.hive.n>=3);")
    rep("'Les abeilles butinent tes fleurs, et lʼune dʼelles suit '+esc(cfg.name)+'. Chaque jour où deux fleurs différentes poussent ici, elles remplissent un rayon.'","'Les abeilles butinent tes fleurs. Chaque jour où deux fleurs différentes poussent ici, elles remplissent un rayon. Quand la ruche est pleine, lʼune dʼelles vient voler près de '+esc(cfg.name)+'.'")
    rep("saveGarden(); openGarden(); toast('Un pot de miel au coffre');","saveGarden(); try{ pepeRender(); }catch(e){} openGarden(); toast('Un pot de miel au coffre');")
    open(path,'w',encoding='utf8').write(s); print('ok',path)
