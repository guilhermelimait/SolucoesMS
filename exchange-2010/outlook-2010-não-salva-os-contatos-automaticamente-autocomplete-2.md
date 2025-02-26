# Outlook 2010 não salva os contatos automaticamente (autocomplete) 2

Date: 2013-10-22 12:03:50

Categories: Exchange 2010

---

<p>Mais uma solução foi encontrada para o fatídico problema relacionado ao Outlook não salvar os contatos automaticamente. E essa solução é simples, porém, conta com um problema no mínimo diferente do normal. Algumas vezes, poucas vezes, quando a conta de correio é migrada entre domínios pode carregar os contatos (internos e externos) em um formato desconhecido. Isso gerará um problema pois nenhum novo ou antigo contato poderá ser salvo até que a solução seja feita. Isso é devido uma importação que o MS Exchange 201o faz para permitir que os contatos sejam desde então disponíveis por parte do servidor, e não mais por um arquivo .nk2.</p>
<p>O arquivo nk2, era um repositório de contatos internos e externos de cada usuário salvo localmente, quando o usuário mudava de máquina, um novo .nk2 era criado e seus contatos não eram importados. No Exchange 2010, ele ainda existe, mas serve apenas como sincronismo para o Exchange 2010, e por isso, em cada máquina que o usuário logar, será possível ter os contatos disponíveis. 🙂</p>
<p>Enfim, vamos a solução:</p>
<p>1 &#8211; Faça o donwload do nk2view <a title="Nk2View" href="http://www.nirsoft.net/utils/outlook_nk2_autocomplete.html" target="_blank">aqui<br />
</a>2- Execute o nk2view e identifique o autocomplete do usuário, geralmente sobre o caminho C:users[Usuário]Application DataMicrosoftOutlook o arquivo deve ter a extensão .nk2<br />
3- Todos os contatos internos e externos ao domínio estarão visíveis. Apague os que forem internos ao domínio.<br />
4- Uma vez apagados, feche o nk2.view, não se preocupe, ele já fez um backup do seu autocomplete, mas você deve salvá-lo quando solicitado.<br />
5- Abra o outlook e tente enviar um email para alguém, o endereço dele ficará salvo, e seus problemas terminaram.</p>
<p>Obrigado pelo contato, e enjoy!</p>
