# Applique les 8 patchs, dans l'ordre, sur chaque fichier donné. S'arrête à la première erreur sans rien laisser à moitié fait.
# Usage : python3 apply_all.py <site>/index.html <manu-ora.html>
import sys, os, shutil, subprocess
here=os.path.dirname(os.path.abspath(__file__))
P=['cloud-patch/cloud_patch.py','scene-patch/scene_patch.py','jeu-patch/jeu_patch.py','dock-patch/dock_patch.py','bee-patch/bee_patch.py','moo-patch/moo_patch.py','sky-patch/sky_patch.py','voyage-patch/voyage_patch.py']
for f in sys.argv[1:]:
    tmp=f+'.tmp-patch'; shutil.copy(f,tmp)
    for p in P:
        r=subprocess.run([sys.executable,os.path.join(here,p),tmp],capture_output=True,text=True)
        if r.returncode!=0:
            os.remove(tmp); sys.exit('ECHEC sur %s avec %s — fichier laissé intact.\n%s'%(f,p,r.stderr[-600:]))
    shutil.move(tmp,f); print('ok',f,'(8 patchs appliqués)')
