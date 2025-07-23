from flask import Blueprint, request, redirect, render_template, url_for, flash,session
from app import db
from app.models.biblia_models import BibliaModel

biblia_bp = Blueprint('biblia', __name__)

@biblia_bp.route('/biblia')
def biblia():# Aqui você pode adicionar lógica para buscar versículos do banco de dados
    versiculos = BibliaModel.query.order_by(BibliaModel.testamento, BibliaModel.versiculo, BibliaModel.capitulo, BibliaModel.livro).all()
    testamentos = db.session.query(BibliaModel.testamento).distinct().all()  # Busca os testamentos distintos
    # Exemplo de busca de todos os versículos

    return render_template('biblia.html',versiculos=versiculos, testamentos=testamentos)

@biblia_bp.route('/I_Reis')
def um_reis():
    # Aqui você pode adicionar lógica para buscar versículos do livro de 1 Reis
    versiculos = BibliaModel.query.filter_by(livro='I_Reis').order_by(BibliaModel.capitulo, BibliaModel.versiculo).all()

    return render_template('I_Reis.html', versiculos=versiculos)

@biblia_bp.route('/Mateus')
def mateus():
    # Aqui você pode adicionar lógica para buscar versículos do livro de Mateus
    versiculos = BibliaModel.query.filter_by(livro='Mateus').order_by(BibliaModel.capitulo, BibliaModel.versiculo).all()

    return render_template('Mateus.html', versiculos=versiculos)

@biblia_bp.route('/cadastro/versiculo', methods=['POST', 'GET'])
def cadastro_versiculo():
    if request.method == 'POST':
        testamento = request.form['testamento']
        livro = request.form['livro']
        capitulo = request.form['capitulo']
        versiculo = request.form['versiculo']
        conteudo = request.form['conteudo']
        
        # Aqui você pode adicionar lógica para salvar o versículo no banco de dados
        novo_versiculo = BibliaModel(testamento=testamento, livro=livro, capitulo=capitulo, versiculo=versiculo, conteudo=conteudo)
        db.session.add(novo_versiculo)
        db.session.commit()
        # Exibir mensagem de sucesso
        flash('Versículo cadastrado com sucesso!', 'success')
        return redirect(url_for('biblia.biblia'))
    
    return render_template('cadastro_versiculo.html')

@biblia_bp.route('/excluir/versiculo/<int:id>', methods=['POST','GET'])
def excluir_versiculo(id):
    versiculo = BibliaModel.query.get_or_404(id)
    db.session.delete(versiculo)
    db.session.commit()
    flash('Versículo excluído com sucesso!', 'success')
    return redirect(url_for('biblia.biblia'))

@biblia_bp.route('/editar/versiculo/<int:id>', methods=['GET', 'POST'])
def editar_versiculo(id):
    versiculo = BibliaModel.query.get_or_404(id)    
    if request.method == 'POST':
        versiculo.testamento = request.form['testamento']
        versiculo.livro = request.form['livro']
        versiculo.capitulo = request.form['capitulo']
        versiculo.versiculo = request.form['versiculo']
        versiculo.conteudo = request.form['conteudo']
        # Aqui você pode adicionar lógica para atualizar o versículo no banco de dados
        db.session.add(versiculo)        
        db.session.commit()
        flash('Versículo atualizado com sucesso!', 'success')
        return redirect(url_for('biblia.biblia'))
    
    return render_template('editar_versiculo.html', versiculo=versiculo)
