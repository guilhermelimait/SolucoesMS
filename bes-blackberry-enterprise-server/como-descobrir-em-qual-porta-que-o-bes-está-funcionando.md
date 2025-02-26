# Como descobrir em qual porta que o BES está funcionando?

Date: 2013-07-29 12:38:18

Categories: BES (Blackberry Enterprise Server)

---

<p>Olá pessoal, e se eu precisar verificar qual a porta que o BES (Blackberry Enterprise Server) está respondendo ao ambiente? Como posso verificar isso?</p>
<p>Fácil!</p>
<p>1- Iniciar &gt;Executar &gt; regedit &gt; OK</p>
<p>2- Vá até a chave [HKEY_LOCAL_MACHINESOFTWAREResearch In MotionBlackBerry Enterprise ServerDispatcher]</p>
<p>3- Procure pela chave &#8220;TcpPort&#8221;=dword:00001005 (1005 = <strong>4101</strong> in hex) ou &#8220;TcpPort&#8221;=dword:00001005 (c1d = <strong>3101</strong> in hex)</p>
<p style="text-align: center;"><a href="http://solucoesms.com.br/wp-content/uploads/2013/07/bes.png"><img loading="lazy" decoding="async" class="aligncenter size-medium wp-image-81" alt="bes" src="http://solucoesms.com.br/wp-content/uploads/2013/07/bes-300x26.png" width="300" height="26" /></a></p>
<p>Enjoy!</p>
<p><object id="38f9fb18-aa2a-8cb8-387a-ba9619a4a2a6" width="0" height="0" type="application/gas-events-abn"></object></p>
