# Outlook 2007 / 2010 / 2013 será descontinuado, mas como fazer para continuar utilizando-o?

Date: 2019-10-15 09:39:39

Categories: O365, Outlook

---

<p>Foi informado pela Microsoft que no dia 13 de Outubro de 2020 as versões de Outlook 2007 / 2010 / 2013 que continuam conectados aos servidores mais atuais não poderão continuar funcionando por incompatibilidade de um protocolo de segurança. Mas, caso ainda seja necessário mantê-lo funcionando por um tempo na sua infraestrutura é possível modificar uma chave no registro que poderá lhe ajudar. Veja abaixo.</p>
<pre>Iniciar &gt; Executar &gt; digite regedit.exe
Navegue até o caminho da chave [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\14.0\Outlook\AutoDiscover] 
Botão direito na pasta e clique em Novo &gt; DWORD (32-bit) }Value
Salve a chave com o nome ExcludeScpLookup, abra a chave e edite o valor para "1" &gt; OK
Reinicie o Outlook</pre>
<p>Prontinho, com isso seu Outlook 2010 continuará conectado por mais algum tempo.<br />
Caso use alguma das outras versões, 2007 ou 2013, troque o 14.0 na chave por aquela da versão que utilize.</p>
