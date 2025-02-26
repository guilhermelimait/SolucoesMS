# Limite de contas simultaneas no Outlook 2010

Date: 2013-10-16 20:11:09

Categories: Outlook

---

<p>Sim, como sempre os nossos lindos usuários nos surpreendem, e como de praxe, algo pra nos adicionar conhecimento. Amo isso.<br />
Dessa vez um usuário tem 13 contas simultâneas abertas no outlook porém elas não atualizam automaticamente, na verdade, somente até a nona caixa adicional é que tudo funciona, mas e aí, o que fazer?</p>
<p>De acordo com o documento da Microsoft <a href="http://blogs.technet.com/b/outlooking/archive/2012/12/24/clarification-on-outlook-2010-and-additional-exchange-account-supportability.aspx">http://blogs.technet.com/b/outlooking/archive/2012/12/24/clarification-on-outlook-2010-and-additional-exchange-account-supportability.aspx</a> o limite é de 10 contas, mas isso é possível ser alterado, e para tal, faremos do seguinte procedimento:</p>
<p>1- Iniciar &gt; Executar &gt; Regedit &gt; OK</p>
<p>2- Acesse a chave HKEY_CURRENT_USER/software/policies/Microsoftexchange</p>
<p>3- Crie a DWORD: MaxNumExchange</p>
<p>4- Insira um número inteiro maior que 10, 20 por exemplo, feche o regedit, reinicie o computador e reabra o Outlook.</p>
<p>Enjoy!</p>
