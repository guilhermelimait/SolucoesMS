# Pesquisar palavras chave em mensagens

Date: 2014-08-11 17:14:45

Categories: Exchange 2007, Exchange 2010, Exchange 2013

---

<p>Olá pessoal,</p>
<p>Caso seja necessário, durante uma operação de investigação é possível identificar todas as mensagens que constarem as palavras solicitadas, assim como definido a seguir, confira:</p>
<blockquote>
<pre>Get-Mailbox -Server "SERVIDOR" -ResultSize unlimited | Search-Mailbox -SearchQuery 'Body:“PALAVRA1” -And “PALAVRA2” -And “PALAVRA 3”' -targetmailbox "guilherme.lima@solucoesms.com.br" -targetfolder "inbox" -loglevel full</pre>
</blockquote>
<p>Dessa forma consigo encontrar todos os e-mails que contiverem as três palavras solicitadas na conta e servidor solicitados. Outra forma de pesquisar é utilizando ao invés de palavras chaves é o remetente, e ainda mais, salvando o resultado em uma conta de pesquisa (que deve ser criada antecipadamente), veja mais:</p>
<blockquote>
<pre>Get-Mailbox guilherme.lima@solucoesms.com.br | Search-Mailbox -SearchQuery 'from:"TESTE@hotmail.com”' -targetmailbox "mailboxinvestigacao@solucoesms.com.br" -targetfolder "investigacao" -loglevel full</pre>
</blockquote>
<p>Espero que ajude! 🙂</p>
<p>Fonte: <a href="https://technet.microsoft.com/en-us/library/dd298173(v=exchg.160).aspx">link</a></p>
<p>&nbsp;</p>
