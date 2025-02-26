# Como verificar qual aplicativo está usando uma porta?

Date: 2020-01-14 09:38:29

Categories: Comando local/PC, Gerenciamento

---

<p><strong>Verificar qual aplicativo está usando a porta:</strong></p>
<blockquote>
<p style="text-align: justify;">1- Abra o prompt de comando &#8211; inicie »execute» cmd ou inicie »Todos os Programas» Acessórios »Prompt de Comando.<br />
2- Digite<strong> netstat -aon | findstr &#8216;[port_number]&#8217;</strong>.</p>
<p style="text-align: justify;">3- Substitua o [port_number] pelo número da porta real que você deseja verificar e pressione enter. Se a porta estiver sendo usada por qualquer aplicativo, os detalhes desse aplicativo serão mostrados. O número, mostrado na última coluna da lista, é o PID (ID do processo) desse aplicativo.<br />
4- Digite<strong> Tasklist | findstr &#8216;[PID]&#8217;</strong>. Substitua o [PID] pelo número da etapa acima e pressione Enter.</p>
</blockquote>
<p style="text-align: justify;"><span style="color: #ff0000;"><strong>Resultado:</strong></span> Você verá o nome do aplicativo que está usando o número da sua porta.</p>
<p>-/-</p>
<p style="text-align: justify;"><strong>Verificando qual porta está sendo usada por um aplicativo:</strong><br />
Este é exatamente o contrário das etapas acima.</p>
<blockquote>
<p style="text-align: justify;">1- Abra o prompt de comando &#8211; inicie »execute» cmd ou inicie »Todos os Programas» Acessórios »Prompt de Comando.<br />
2- Digite <strong>tasklist | findstr &#8216;[nome_aplicativo]&#8217;</strong>. Substitua [application_name] pelo aplicativo que você deseja verificar (por exemplo, apache) e pressione enter.<br />
3- Anote o PID (segunda coluna) com os detalhes mostrados.<br />
4- Digite <strong>netstat -aon | findstr &#8216;[PID]&#8217;</strong>. Substitua o [PID] da etapa acima e pressione Enter.</p>
</blockquote>
<p style="text-align: justify;"><span style="color: #ff0000;"><strong>Resultado:</strong></span> Você verá os detalhes do aplicativo e a porta correspondente à qual está ouvindo.</p>
<p style="text-align: justify;">Fonte: <a href="https://veerasundar.com/blog/2009/10/how-to-check-which-application-is-using-which-port/">Veerasundar</a></p>
<p style="text-align: justify;">
