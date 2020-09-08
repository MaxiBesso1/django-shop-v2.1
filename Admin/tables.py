PRODUCTS_TABLE = """
<div class="row">
    <div class="col-1 col-md-3"></div>
    <div class="col-10 col-md-6">
        <h4>{{name}}
            <div class="ml-auto">
                <a href="" class="btn btn-primary btn-rounded">Nuevo</a>
            </div>
        </h4>
        <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Nombre</th>
                  <th scope="col">Precio</th>
                  <th scope="col">Estado</th>
                  <th scope="col">Categoria</th>
                  <th scope="col">Fecha de subida</th>
                  <th scope="col"></th> 
                </tr>
              </thead>
              <tbody>
                {% for x in objects %}
                <tr>
                    <th scope="row">{{x.name}}</th>
                    <th scope="row">{{x.price}}</th>
                    {% if x.offer %}
                    <th scope="row">En oferta <span class="text-warning">{{x.new_price}}</span>/{{x.price}}</th>
                    {% else %}
                    <th scope="row">Por defecto</span>/{{x.price}}</th>
                    {% endif %}
                    <th scope="row">{{x.category}}</th>
                    <th scope="row">{{x.date}}</th>
                    <th scope="row">
                        <a href="edit" class="btn btn-primary btn-rounded">Editar</a>
                        <a href="edit" class="btn btn-danger btn-rounded">Eliminar</a>
                    </th>
                </tr>
                {% endfor %}
              </tbody>
            </table>
          </div>
    </div>
    <div class="col-1 col-md-3"></div>
</div>
"""
CATEGORY_TABLE = """
<div class="row">
    <div class="col-1 col-md-3"></div>
    <div class="col-10 col-md-6">
        <h4>{{name}}
            <div class="ml-auto">
                <a href="" class="btn btn-primary btn-rounded">Nuevo</a>
            </div>
        </h4>
        <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Nombre</th>
                  <th scope="col"></th> 
                </tr>
              </thead>
              <tbody>
                {% for x in objects %}
                <tr>
                    <th scope="row">{{x.name}}</th>
                    <th scope="row">
                        <a href="edit" class="btn btn-primary btn-rounded">Editar</a>
                        <a href="edit" class="btn btn-danger btn-rounded">Eliminar</a>
                    </th>
                </tr>
                {% endfor %}
              </tbody>
            </table>
          </div>
    </div>
    <div class="col-1 col-md-3"></div>
</div>
"""

STYLES_TABLE = """
<div class="row">
    <div class="col-1 col-md-3"></div>
    <div class="col-10 col-md-6">
        <h4>{{name}}
            <div class="ml-auto">
                <a href="" class="btn btn-primary btn-rounded">Editar estilos</a>
            </div>
        </h4>
        <div class="table-responsive">
            <table class="table">
              <thead>
                <tr>
                    <th scope="row">Titulo 1 </th>
                    <th scope="row">Titulo 2 </th>
                    <th scope="row">Titulo 3 </th>
                    <th scope="row"> Color del titulo 1 </th>
                    <th scope="row"> Color del titulo 2 </th>
                    <th scope="row"> Color del titulo 3 </th>
                    
                </tr>
              </thead>
              <tbody>
                {% for x in objects %}
                <tr>
                    <th scope="row">{{x.title}}</th>
                    <th scope="row">{{x.title_2}}</th>
                    <th scope="row">{{x.title_3}}</th>
                    <th scope="row">{{x.title_color}}</th>
                    <th scope="row">{{x.title_color_2}}</th>
                    <th scope="row">{{x.title_color_3}}</th>
                </tr>
              </tbody>
            </table>
            <div class="mt-3">
                <div class="table-responsive">
                    <table class="table">
                      <thead>
                        <tr>
                            
                            <th scope="row">Subitulo 1 </th>
                            <th scope="row">Subtitulo 2 </th>
                            <th scope="row">Subtitulo 3 </th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                            <th scope="row">{{x.subtitle}}</th>
                            <th scope="row">{{x.subtitle_2}}</th>
                            <th scope="row">{{x.subtitle_3}}</th>
                            <th scope="row">{{x.subtitle_color}}</th>
                            <th scope="row">{{x.subtitle_color_2}}</th>
                            <th scope="row">{{x.subtitle_color_3}}</th>
                        </tr>
                      </tbody>
                    </table>
            </div>
          </div>
          <div class="mt-3">
            <div class="table-responsive">
                <table class="table">
                  <thead>
                    <tr>
                        <th scope="row">Imagen del banner 1 </th>
                        <th scope="row">Imagen del banner 2 </th>
                        <th scope="row">Imagen del banner 3 </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                        <th scope="row">{{x.status}}</th>
                        <th scope="row">{{x.status_2}}</th>
                        <th scope="row">{{x.status_3}}</th>
                    </tr>
                    {% endfor %}
                  </tbody>
                </table>
        </div>
      </div>
    </div>
    <div class="col-1 col-md-3"></div>
</div>"""