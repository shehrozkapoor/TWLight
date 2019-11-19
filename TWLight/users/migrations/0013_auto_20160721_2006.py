# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [("users", "0012_editor_wp_valid")]

    operations = [
        migrations.AlterField(
            model_name="editor",
            name="home_wiki",
            field=models.CharField(
                help_text="Home wiki, as indicated by user",
                max_length=4,
                choices=[
                    (b"aa", b"aa.wikipedia.org"),
                    (b"ab", b"ab.wikipedia.org"),
                    (b"ace", b"ace.wikipedia.org"),
                    (b"af", b"af.wikipedia.org"),
                    (b"ak", b"ak.wikipedia.org"),
                    (b"als", b"als.wikipedia.org"),
                    (b"am", b"am.wikipedia.org"),
                    (b"an", b"an.wikipedia.org"),
                    (b"ang", b"ang.wikipedia.org"),
                    (b"ar", b"ar.wikipedia.org"),
                    (b"arc", b"arc.wikipedia.org"),
                    (b"arz", b"arz.wikipedia.org"),
                    (b"as", b"as.wikipedia.org"),
                    (b"ast", b"ast.wikipedia.org"),
                    (b"av", b"av.wikipedia.org"),
                    (b"ay", b"ay.wikipedia.org"),
                    (b"az", b"az.wikipedia.org"),
                    (b"azb", b"azb.wikipedia.org"),
                    (b"ba", b"ba.wikipedia.org"),
                    (b"bar", b"bar.wikipedia.org"),
                    (b"bat-smg", b"bat-smg.wikipedia.org"),
                    (b"bcl", b"bcl.wikipedia.org"),
                    (b"be", b"be.wikipedia.org"),
                    (b"be-x-old", b"be-x-old.wikipedia.org"),
                    (b"bg", b"bg.wikipedia.org"),
                    (b"bh", b"bh.wikipedia.org"),
                    (b"bi", b"bi.wikipedia.org"),
                    (b"bjn", b"bjn.wikipedia.org"),
                    (b"bm", b"bm.wikipedia.org"),
                    (b"bn", b"bn.wikipedia.org"),
                    (b"bo", b"bo.wikipedia.org"),
                    (b"bpy", b"bpy.wikipedia.org"),
                    (b"br", b"br.wikipedia.org"),
                    (b"bs", b"bs.wikipedia.org"),
                    (b"bug", b"bug.wikipedia.org"),
                    (b"bxr", b"bxr.wikipedia.org"),
                    (b"ca", b"ca.wikipedia.org"),
                    (b"cbk-zam", b"cbk-zam.wikipedia.org"),
                    (b"cdo", b"cdo.wikipedia.org"),
                    (b"ce", b"ce.wikipedia.org"),
                    (b"ceb", b"ceb.wikipedia.org"),
                    (b"ch", b"ch.wikipedia.org"),
                    (b"cho", b"cho.wikipedia.org"),
                    (b"chr", b"chr.wikipedia.org"),
                    (b"chy", b"chy.wikipedia.org"),
                    (b"ckb", b"ckb.wikipedia.org"),
                    (b"co", b"co.wikipedia.org"),
                    (b"cr", b"cr.wikipedia.org"),
                    (b"crh", b"crh.wikipedia.org"),
                    (b"cs", b"cs.wikipedia.org"),
                    (b"csb", b"csb.wikipedia.org"),
                    (b"cu", b"cu.wikipedia.org"),
                    (b"cv", b"cv.wikipedia.org"),
                    (b"cy", b"cy.wikipedia.org"),
                    (b"da", b"da.wikipedia.org"),
                    (b"de", b"de.wikipedia.org"),
                    (b"diq", b"diq.wikipedia.org"),
                    (b"dsb", b"dsb.wikipedia.org"),
                    (b"dv", b"dv.wikipedia.org"),
                    (b"dz", b"dz.wikipedia.org"),
                    (b"ee", b"ee.wikipedia.org"),
                    (b"el", b"el.wikipedia.org"),
                    (b"eml", b"eml.wikipedia.org"),
                    (b"en", b"en.wikipedia.org"),
                    (b"eo", b"eo.wikipedia.org"),
                    (b"es", b"es.wikipedia.org"),
                    (b"et", b"et.wikipedia.org"),
                    (b"eu", b"eu.wikipedia.org"),
                    (b"ext", b"ext.wikipedia.org"),
                    (b"fa", b"fa.wikipedia.org"),
                    (b"ff", b"ff.wikipedia.org"),
                    (b"fi", b"fi.wikipedia.org"),
                    (b"fiu-vro", b"fiu-vro.wikipedia.org"),
                    (b"fj", b"fj.wikipedia.org"),
                    (b"fo", b"fo.wikipedia.org"),
                    (b"fr", b"fr.wikipedia.org"),
                    (b"frp", b"frp.wikipedia.org"),
                    (b"frr", b"frr.wikipedia.org"),
                    (b"fur", b"fur.wikipedia.org"),
                    (b"fy", b"fy.wikipedia.org"),
                    (b"ga", b"ga.wikipedia.org"),
                    (b"gag", b"gag.wikipedia.org"),
                    (b"gan", b"gan.wikipedia.org"),
                    (b"gd", b"gd.wikipedia.org"),
                    (b"gl", b"gl.wikipedia.org"),
                    (b"glk", b"glk.wikipedia.org"),
                    (b"gn", b"gn.wikipedia.org"),
                    (b"gom", b"gom.wikipedia.org"),
                    (b"got", b"got.wikipedia.org"),
                    (b"gu", b"gu.wikipedia.org"),
                    (b"gv", b"gv.wikipedia.org"),
                    (b"ha", b"ha.wikipedia.org"),
                    (b"hak", b"hak.wikipedia.org"),
                    (b"haw", b"haw.wikipedia.org"),
                    (b"he", b"he.wikipedia.org"),
                    (b"hi", b"hi.wikipedia.org"),
                    (b"hif", b"hif.wikipedia.org"),
                    (b"ho", b"ho.wikipedia.org"),
                    (b"hr", b"hr.wikipedia.org"),
                    (b"hsb", b"hsb.wikipedia.org"),
                    (b"ht", b"ht.wikipedia.org"),
                    (b"hu", b"hu.wikipedia.org"),
                    (b"hy", b"hy.wikipedia.org"),
                    (b"hz", b"hz.wikipedia.org"),
                    (b"ia", b"ia.wikipedia.org"),
                    (b"id", b"id.wikipedia.org"),
                    (b"ie", b"ie.wikipedia.org"),
                    (b"ig", b"ig.wikipedia.org"),
                    (b"ii", b"ii.wikipedia.org"),
                    (b"ik", b"ik.wikipedia.org"),
                    (b"ilo", b"ilo.wikipedia.org"),
                    (b"io", b"io.wikipedia.org"),
                    (b"is", b"is.wikipedia.org"),
                    (b"it", b"it.wikipedia.org"),
                    (b"iu", b"iu.wikipedia.org"),
                    (b"ja", b"ja.wikipedia.org"),
                    (b"jbo", b"jbo.wikipedia.org"),
                    (b"jv", b"jv.wikipedia.org"),
                    (b"ka", b"ka.wikipedia.org"),
                    (b"kaa", b"kaa.wikipedia.org"),
                    (b"kab", b"kab.wikipedia.org"),
                    (b"kbd", b"kbd.wikipedia.org"),
                    (b"kg", b"kg.wikipedia.org"),
                    (b"ki", b"ki.wikipedia.org"),
                    (b"kj", b"kj.wikipedia.org"),
                    (b"kk", b"kk.wikipedia.org"),
                    (b"kl", b"kl.wikipedia.org"),
                    (b"km", b"km.wikipedia.org"),
                    (b"kn", b"kn.wikipedia.org"),
                    (b"ko", b"ko.wikipedia.org"),
                    (b"koi", b"koi.wikipedia.org"),
                    (b"kr", b"kr.wikipedia.org"),
                    (b"krc", b"krc.wikipedia.org"),
                    (b"ks", b"ks.wikipedia.org"),
                    (b"ksh", b"ksh.wikipedia.org"),
                    (b"ku", b"ku.wikipedia.org"),
                    (b"kv", b"kv.wikipedia.org"),
                    (b"kw", b"kw.wikipedia.org"),
                    (b"ky", b"ky.wikipedia.org"),
                    (b"la", b"la.wikipedia.org"),
                    (b"lad", b"lad.wikipedia.org"),
                    (b"lb", b"lb.wikipedia.org"),
                    (b"lbe", b"lbe.wikipedia.org"),
                    (b"lez", b"lez.wikipedia.org"),
                    (b"lg", b"lg.wikipedia.org"),
                    (b"li", b"li.wikipedia.org"),
                    (b"lij", b"lij.wikipedia.org"),
                    (b"lmo", b"lmo.wikipedia.org"),
                    (b"ln", b"ln.wikipedia.org"),
                    (b"lo", b"lo.wikipedia.org"),
                    (b"lrc", b"lrc.wikipedia.org"),
                    (b"lt", b"lt.wikipedia.org"),
                    (b"ltg", b"ltg.wikipedia.org"),
                    (b"lv", b"lv.wikipedia.org"),
                    (b"mai", b"mai.wikipedia.org"),
                    (b"map-bms", b"map-bms.wikipedia.org"),
                    (b"mdf", b"mdf.wikipedia.org"),
                    (b"mg", b"mg.wikipedia.org"),
                    (b"mh", b"mh.wikipedia.org"),
                    (b"mhr", b"mhr.wikipedia.org"),
                    (b"mi", b"mi.wikipedia.org"),
                    (b"min", b"min.wikipedia.org"),
                    (b"mk", b"mk.wikipedia.org"),
                    (b"ml", b"ml.wikipedia.org"),
                    (b"mn", b"mn.wikipedia.org"),
                    (b"mo", b"mo.wikipedia.org"),
                    (b"mr", b"mr.wikipedia.org"),
                    (b"mrj", b"mrj.wikipedia.org"),
                    (b"ms", b"ms.wikipedia.org"),
                    (b"mt", b"mt.wikipedia.org"),
                    (b"mus", b"mus.wikipedia.org"),
                    (b"mwl", b"mwl.wikipedia.org"),
                    (b"my", b"my.wikipedia.org"),
                    (b"myv", b"myv.wikipedia.org"),
                    (b"mzn", b"mzn.wikipedia.org"),
                    (b"na", b"na.wikipedia.org"),
                    (b"nah", b"nah.wikipedia.org"),
                    (b"nap", b"nap.wikipedia.org"),
                    (b"nds", b"nds.wikipedia.org"),
                    (b"nds-nl", b"nds-nl.wikipedia.org"),
                    (b"ne", b"ne.wikipedia.org"),
                    (b"new", b"new.wikipedia.org"),
                    (b"ng", b"ng.wikipedia.org"),
                    (b"nl", b"nl.wikipedia.org"),
                    (b"nn", b"nn.wikipedia.org"),
                    (b"no", b"no.wikipedia.org"),
                    (b"nov", b"nov.wikipedia.org"),
                    (b"nrm", b"nrm.wikipedia.org"),
                    (b"nso", b"nso.wikipedia.org"),
                    (b"nv", b"nv.wikipedia.org"),
                    (b"ny", b"ny.wikipedia.org"),
                    (b"oc", b"oc.wikipedia.org"),
                    (b"om", b"om.wikipedia.org"),
                    (b"or", b"or.wikipedia.org"),
                    (b"os", b"os.wikipedia.org"),
                    (b"pa", b"pa.wikipedia.org"),
                    (b"pag", b"pag.wikipedia.org"),
                    (b"pam", b"pam.wikipedia.org"),
                    (b"pap", b"pap.wikipedia.org"),
                    (b"pcd", b"pcd.wikipedia.org"),
                    (b"pdc", b"pdc.wikipedia.org"),
                    (b"pfl", b"pfl.wikipedia.org"),
                    (b"pi", b"pi.wikipedia.org"),
                    (b"pih", b"pih.wikipedia.org"),
                    (b"pl", b"pl.wikipedia.org"),
                    (b"pms", b"pms.wikipedia.org"),
                    (b"pnb", b"pnb.wikipedia.org"),
                    (b"pnt", b"pnt.wikipedia.org"),
                    (b"ps", b"ps.wikipedia.org"),
                    (b"pt", b"pt.wikipedia.org"),
                    (b"qu", b"qu.wikipedia.org"),
                    (b"rm", b"rm.wikipedia.org"),
                    (b"rmy", b"rmy.wikipedia.org"),
                    (b"rn", b"rn.wikipedia.org"),
                    (b"ro", b"ro.wikipedia.org"),
                    (b"roa-rup", b"roa-rup.wikipedia.org"),
                    (b"roa-tara", b"roa-tara.wikipedia.org"),
                    (b"ru", b"ru.wikipedia.org"),
                    (b"rue", b"rue.wikipedia.org"),
                    (b"rw", b"rw.wikipedia.org"),
                    (b"sa", b"sa.wikipedia.org"),
                    (b"sah", b"sah.wikipedia.org"),
                    (b"sc", b"sc.wikipedia.org"),
                    (b"scn", b"scn.wikipedia.org"),
                    (b"sco", b"sco.wikipedia.org"),
                    (b"sd", b"sd.wikipedia.org"),
                    (b"se", b"se.wikipedia.org"),
                    (b"sg", b"sg.wikipedia.org"),
                    (b"sh", b"sh.wikipedia.org"),
                    (b"si", b"si.wikipedia.org"),
                    (b"simple", b"simple.wikipedia.org"),
                    (b"sk", b"sk.wikipedia.org"),
                    (b"sl", b"sl.wikipedia.org"),
                    (b"sm", b"sm.wikipedia.org"),
                    (b"sn", b"sn.wikipedia.org"),
                    (b"so", b"so.wikipedia.org"),
                    (b"sq", b"sq.wikipedia.org"),
                    (b"sr", b"sr.wikipedia.org"),
                    (b"srn", b"srn.wikipedia.org"),
                    (b"ss", b"ss.wikipedia.org"),
                    (b"st", b"st.wikipedia.org"),
                    (b"stq", b"stq.wikipedia.org"),
                    (b"su", b"su.wikipedia.org"),
                    (b"sv", b"sv.wikipedia.org"),
                    (b"sw", b"sw.wikipedia.org"),
                    (b"szl", b"szl.wikipedia.org"),
                    (b"ta", b"ta.wikipedia.org"),
                    (b"te", b"te.wikipedia.org"),
                    (b"tet", b"tet.wikipedia.org"),
                    (b"tg", b"tg.wikipedia.org"),
                    (b"th", b"th.wikipedia.org"),
                    (b"ti", b"ti.wikipedia.org"),
                    (b"tk", b"tk.wikipedia.org"),
                    (b"tl", b"tl.wikipedia.org"),
                    (b"tn", b"tn.wikipedia.org"),
                    (b"to", b"to.wikipedia.org"),
                    (b"tpi", b"tpi.wikipedia.org"),
                    (b"tr", b"tr.wikipedia.org"),
                    (b"ts", b"ts.wikipedia.org"),
                    (b"tt", b"tt.wikipedia.org"),
                    (b"tum", b"tum.wikipedia.org"),
                    (b"tw", b"tw.wikipedia.org"),
                    (b"ty", b"ty.wikipedia.org"),
                    (b"tyv", b"tyv.wikipedia.org"),
                    (b"udm", b"udm.wikipedia.org"),
                    (b"ug", b"ug.wikipedia.org"),
                    (b"uk", b"uk.wikipedia.org"),
                    (b"ur", b"ur.wikipedia.org"),
                    (b"uz", b"uz.wikipedia.org"),
                    (b"ve", b"ve.wikipedia.org"),
                    (b"vec", b"vec.wikipedia.org"),
                    (b"vep", b"vep.wikipedia.org"),
                    (b"vi", b"vi.wikipedia.org"),
                    (b"vls", b"vls.wikipedia.org"),
                    (b"vo", b"vo.wikipedia.org"),
                    (b"wa", b"wa.wikipedia.org"),
                    (b"war", b"war.wikipedia.org"),
                    (b"wo", b"wo.wikipedia.org"),
                    (b"wuu", b"wuu.wikipedia.org"),
                    (b"xal", b"xal.wikipedia.org"),
                    (b"xh", b"xh.wikipedia.org"),
                    (b"xmf", b"xmf.wikipedia.org"),
                    (b"yi", b"yi.wikipedia.org"),
                    (b"yo", b"yo.wikipedia.org"),
                    (b"za", b"za.wikipedia.org"),
                    (b"zea", b"zea.wikipedia.org"),
                    (b"zh", b"zh.wikipedia.org"),
                    (b"zh-classical", b"zh-classical.wikipedia.org"),
                    (b"zh-min-nan", b"zh-min-nan.wikipedia.org"),
                    (b"zh-yue", b"zh-yue.wikipedia.org"),
                    (b"zu", b"zu.wikipedia.org"),
                ],
            ),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name="editor", unique_together=set([("wp_username", "home_wiki")])
        ),
    ]
