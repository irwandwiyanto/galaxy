define(["utils/utils","mvc/tools/tools-form-base"],function(b,a){var c=a.extend({initialize:function(d){this.workflow=true;a.prototype.initialize.call(this,d)},_buildModel:function(){},_updateModel:function(){var d=this;var e=this.tree.finalize();console.debug("tools-form-workflow::_refreshForm() - Refreshing states.");console.debug(e);var g=this.deferred.register();var f=galaxy_config.root+"workflow/editor_form_post?tool_id="+this.options.id;b.request({type:"GET",url:f,data:e,success:function(h){parent.update_node(h);d.deferred.done(g);console.debug("tools-form::_refreshForm() - States refreshed.");console.debug(h)},error:function(h){d.deferred.done(g);console.debug("tools-form::_refreshForm() - Refresh request failed.");console.debug(h)}})}});return{View:c}});