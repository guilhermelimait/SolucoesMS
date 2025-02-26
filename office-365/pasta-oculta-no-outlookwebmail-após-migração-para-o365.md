# Pasta oculta no outlook/webmail após migração para O365

Date: 2018-01-25 18:50:48

Categories: Office 365

---

<p>Ladies and Gentleman!</p>
<p>Após a migração de um usuário para o O365, uma de suas pastas desapareceu, apesar de seus arquivos/mails aparecerem em pesquisas e via shell, não era possível visualizar a pasta em si. Para isso faremos o download de uma ferramenta de terceiros.</p>
<p>Baixe o MFCMAPI <a href="https://github.com/stephenegriffin/mfcmapi/releases/tag/17.0.17099.01">aqui</a>.</p>
<p>Após o download, extraia o arquivo e abra o MFCMAPI.exe.<br />
Clique em OK<br />
Clique em SESSION &gt; LOGON<br />
Selecione o perfil configurado &gt; OK<br />
Clique duas vezes na conta configurada &gt; OK<br />
Na nova janela aberta &gt; Raiz &gt; IPM_SUBTREE &gt; Selecione a pasta que está desaparecida<br />
Do lado direito, procure a chave PR_ATTR_HIDDEN &gt; abra a chave e desmarque a opção HIDDEN<br />
OK &gt; feche tudo.</p>
<p>Abra o outlook e voilá!</p>
<p><!--more--></p>
<p>Caso sejam todas as imagens, verifique se por acaso não é apenas uma questão de alterar a visibilidade do conteúdo da pasta:</p>
<p>Exibir &gt; Alterar modo de exibição &gt; selecione Mensagens Imap</p>
<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-912" src="http://solucoesms.com.br/wp-content/uploads/2018/01/pastas.png" alt="" width="535" height="278" srcset="https://solucoesms.com.br/wp-content/uploads/2018/01/pastas.png 535w, https://solucoesms.com.br/wp-content/uploads/2018/01/pastas-300x156.png 300w" sizes="auto, (max-width: 535px) 100vw, 535px" /></p>
<p>&nbsp;</p>
<p>Enjoy!</p>
