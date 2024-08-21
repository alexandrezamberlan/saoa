from django import forms

from evento.models import Evento
from submissao.models import Submissao
from usuario.models import Usuario


class MembroCreateForm(forms.ModelForm):
    #(técnico, graduando, graduado, especialista, mestre, doutor)
    TITULACAO = (
        ('TECNICO', 'Técnico'),
        ('GRADUANDO', 'Graduando' ),
        ('GRADUADO', 'Graduado' ),        
        ('ESPECIALISTA', 'Especialista'),
        ('MESTRE', 'Mestre' ),
        ('DOUTOR', 'Doutor' ),        
    )

    #(Ciências Humana, Ciências da Saúde, Ciências Sociais, Ciências Tecnológicas)
    AREA = (
        ('HUMANAS', 'Ciências Humanas'),
        ('SAUDE', 'Ciências da Saúde' ),
        ('SOCIAIS', 'Ciências Sociais' ),        
        ('TECNOLOGICA', 'Ciências Tecnológicas'),        
    )

    nome = forms.CharField(label='Nome completo *', help_text='* Campos obrigatórios',required=True)
    titulacao = forms.ChoiceField(label='Titulação *',choices=TITULACAO, help_text='Selecione a maior titulação', required=False)
    area = forms.ChoiceField(label='Área de pesquisa do usuário *', choices=AREA, help_text='Escolha área de interesse de trabalho',required=True)
    instituicao = forms.CharField(label='Instituição a que pertence *', help_text='Registre a instituição, ou universidade, ou empresa',required=True)
    email = forms.EmailField(label='Email *', help_text='Use o email válido. Será usado para acessar sistema e recuperar senha!',required=True)
    celular = forms.CharField(label='Número celular com DDD *', help_text="Use DDD, por exemplo 55987619832",required=True)
    cpf = forms.CharField(label='CPF *',required=True)    
    
        
    class Meta:
        model = Usuario
        fields = ['nome','titulacao', 'area', 'instituicao', 'email', 'celular', 'cpf']


class SubmissaoForm(forms.ModelForm):
    evento = forms.ModelChoiceField(label='Evento para a submissão *', queryset=Evento.eventos_ativos_data_aberta.all(), required=True)   
 
    class Meta:
        model = Submissao
        fields = ['evento', 'titulo', 'resumo' , 'abstract', 'palavras_chave', 'arquivo_sem_autores', 'arquivo_final', 
                  'arquivo_comite_etica', 'observacoes']

    # def clean_colaborador(self):
    #     colaborador = self.cleaned_data.get('colaborador')
    #     responsavel = self.cleaned_data.get('responsavel')

    #     if (responsavel in colaborador.all()):
    #         raise forms.ValidationError('Um membro não pode ser ao mesmo tempo responsável e colaborador')
    #     return colaborador


class BuscaSubmissaoForm(forms.Form):     
    STATUS = (
        (None, '-----------'),
        ('EM EDICAO', 'Em edição'),
        ('EM ANALISE', 'Em análise'),
        ('EM CORRECAO', 'Em correção' ),        
        ('APROVADO', 'Aprovado' ),
        ('RETIRADO PELO RESPONSAVEL', 'Retirado pelo responsável'),
        ('RETIRADO PELO COORDENADOR', 'Retirado pelo coordenador' ),
        ('REPROVADO', 'Reprovado' ),  
    )         
    
    situacao = forms.ChoiceField(label='Status da submissão', choices=STATUS, required=False)
    pesquisa = forms.CharField(label='Pesquisa livre', required=False)
    
    
class MinhaAvaliacaoResponsavelForm(forms.ModelForm):
    parecer_avaliador_responsavel = forms.CharField(label='Parecer do avaliador 1 (5000 caracteres)', max_length=5000, widget=forms.widgets.Textarea(), help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    parecer_rebanca_avaliador_responsavel = forms.CharField(label='Parecer de rebanca do avaliador 1 (5000 caracteres)', max_length=5000, widget=forms.widgets.Textarea(),  help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!', required=False)
    merito_desenvolvimento_responsavel = forms.DecimalField(label='Desenvolvimento',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merito_redacao_responsavel = forms.DecimalField(label='Redação do texto',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merito_apresentacao_responsavel = forms.DecimalField(label='Apresentação',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    nota_final_responsavel = forms.DecimalField(label='Final responsavel',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])    
    arquivo_corrigido_responsavel = forms.FileField(label='Arquivo do TCC corrigido pelo avaliador 1',  help_text='Use formato .pdf para enviar seu arquivo corrigido', required=False)
    
    
    class Meta:
        model = Avaliacao
        fields = ['parecer_avaliador_responsavel', 'parecer_rebanca_avaliador_responsavel', 
              'merito_desenvolvimento_responsavel', 'merito_redacao_responsavel',
              'merito_apresentacao_responsavel','arquivo_corrigido_responsavel', 'nota_final_responsavel']
        
        
class MinhaAvaliacaoSuplenteForm(forms.ModelForm):
    parecer_avaliador_suplente = forms.CharField(label='Parecer do avaliador 2 (5000 caracteres)', max_length=5000, widget=forms.widgets.Textarea(), help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    parecer_rebanca_avaliador_suplente = forms.CharField(label='Parecer de rebanca do avaliador 2 (5000 caracteres)', max_length=5000, widget=forms.widgets.Textarea(),  help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!', required=False)
    merito_desenvolvimento_suplente = forms.DecimalField(label='Desenvolvimento',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merito_redacao_suplente = forms.DecimalField(label='Redação do texto',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merito_apresentacao_suplente = forms.DecimalField(label='Apresentação',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    nota_final_suplente = forms.DecimalField(label='Final suplente',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])    
    arquivo_corrigido_suplente = forms.FileField(label='Arquivo do TCC corrigido pelo avaliador 2', help_text='Use formato .pdf para enviar seu arquivo corrigido', required=False)
    
    
    class Meta:
        model = Avaliacao
        fields = ['parecer_avaliador_suplente', 'parecer_rebanca_avaliador_suplente',
              'merito_desenvolvimento_suplente', 'merito_redacao_suplente',
              'merito_apresentacao_suplente','arquivo_corrigido_suplente', 'nota_final_suplente']
        
        
class MinhaAvaliacaoConvidadoForm(forms.ModelForm):
    parecer_avaliador_convidado = forms.CharField(label='Parecer do avaliador convidado (5000 caracteres)', max_length=5000, widget=forms.widgets.Textarea(), help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!')
    parecer_rebanca_avaliador_convidado = forms.CharField(label='Parecer de rebanca do avaliador convidado (5000 caracteres)', max_length=5000, widget=forms.widgets.Textarea(),  help_text='Atenção: se colar seu texto no campo, confira se ele coube no espaço!!', required=False)
    merito_desenvolvimento_convidado = forms.DecimalField(label='Desenvolvimento',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merito_redacao_convidado = forms.DecimalField(label='Redação do texto',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    merito_apresentacao_convidado = forms.DecimalField(label='Apresentação',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    nota_final_convidado = forms.DecimalField(label='Final convidado',help_text='Máximo 10 pontos', max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])    
    arquivo_corrigido_convidado = forms.FileField(label='Arquivo do TCC corrigido pelo avaliador convidado', help_text='Use formato .pdf para enviar seu arquivo corrigido', required=False)
    
    
    class Meta:
        model = Avaliacao
        fields = ['parecer_avaliador_convidado',  'parecer_rebanca_avaliador_convidado', 
              'merito_desenvolvimento_convidado', 'merito_redacao_convidado',
              'merito_apresentacao_convidado','arquivo_corrigido_convidado', 'nota_final_convidado']
        

class MinhaSugestaoPreProjetoForm(forms.ModelForm):
    class Meta:
        model = Submissao
        fields = ['sugestoes_preprojeto']


class BuscaPreProjetoForm(forms.Form):
    nome_aluno = forms.CharField(label='Nome do aluno', required=False)
    curso = forms.ModelChoiceField(label='Curso', queryset=Curso.objects.all(), required=False)
    nome_orientador = forms.CharField(label='Nome do orientador', required=False)
    

class BuscaMinhasAvaliacoesForm(forms.Form):
    STATUS_SUBMISSAO = (
        
        ('EM ANDAMENTO', 'Em andamento'),
        ('ABANDONO OU TRANCADO', 'Abandono ou Trancado'),
        ('FINALIZADO', 'Finalizado'),
        ('REPROVADO', 'Reprovado'),
    ) 
    nome_aluno = forms.CharField(label='Nome do aluno', required=False)
    curso = forms.ModelChoiceField(label='Curso', queryset=Curso.objects.all(), required=False)
    status = forms.ChoiceField(label='Status', choices=STATUS_SUBMISSAO, required=False)
    
    
class BuscaMeusOrientandosForm(forms.Form):
    STATUS_SUBMISSAO = (

        ('EM ANDAMENTO', 'Em andamento'),
        ('ABANDONO OU TRANCADO', 'Abandono ou Trancado'),
        ('FINALIZADO', 'Finalizado'),
        ('REPROVADO', 'Reprovado'),
    ) 
    nome_aluno = forms.CharField(label='Nome do aluno', required=False)
    curso = forms.ModelChoiceField(label='Curso', queryset=Curso.objects.all(), required=False)
    status = forms.ChoiceField(label='Status', choices=STATUS_SUBMISSAO,required=False)