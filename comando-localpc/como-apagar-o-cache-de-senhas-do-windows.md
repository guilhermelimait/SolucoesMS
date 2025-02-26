# Como apagar o cache de senhas do Windows?

Date: 2013-07-17 12:58:36

Categories: Comando local/PC

---

<p>Como apagar o cache de senhas do Windows, e principalmente quando tudo está bloqueado? Tudo mesmo, você não consegue abrir o painel de controle para acessar o Windows Credentials, não consegue elevar seu acesso, ou seja, nada, nada, nada.</p>
<p>Para isso, vá em Iniciar &gt; Executar e digite a seguinte linha de comando:</p>
<blockquote>
<pre id="imcontent">rundll32.exe keymgr.dll, KRShowKeyMgr</pre>
</blockquote>
<div>Aparecerá a janela abaixo, selecione todas as contas e remova todas as entradas. Dessa forma o cache de senha que pode estar atrapalhando seu Outlook pode ser removido com sucesso!</div>
<div></div>
<div><a href="http://solucoesms.com.br/wp-content/uploads/2013/07/pwsd.png"><img loading="lazy" decoding="async" class="aligncenter size-medium wp-image-67" src="http://solucoesms.com.br/wp-content/uploads/2013/07/pwsd-300x295.png" alt="pwsd" width="300" height="295" /></a></div>
<div></div>
<div>Enjoy!</div>
