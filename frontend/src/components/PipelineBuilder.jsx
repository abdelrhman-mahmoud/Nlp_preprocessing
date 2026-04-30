import React from 'react';
import { DragDropContext, Droppable, Draggable } from '@hello-pangea/dnd';
import { GripVertical, X, ArrowUp, ArrowDown } from 'lucide-react';

const PipelineBuilder = ({ steps, setSteps, autoOrder }) => {
  const handleDragEnd = (result) => {
    if (!result.destination) return;
    const items = Array.from(steps);
    const [moved] = items.splice(result.source.index, 1);
    items.splice(result.destination.index, 0, moved);
    setSteps(items);
  };

  const removeStep = (index) =>
    setSteps(steps.filter((_, i) => i !== index));

  const moveStep = (index, dir) => {
    const target = index + dir;
    if (target < 0 || target >= steps.length) return;
    const items = [...steps];
    [items[index], items[target]] = [items[target], items[index]];
    setSteps(items);
  };

  if (steps.length === 0) {
    return (
      <div className="section">
        <div className="section-title">🔗 Pipeline Order</div>
        <div className="pipeline-empty">
          ⬆️ Select functions above to build your pipeline
        </div>
      </div>
    );
  }

  return (
    <div className="section">
      <div className="section-title">
        🔗 Pipeline Order ({steps.length} steps)
        {autoOrder && (
          <span className="badge" style={{ marginInlineStart: 'auto', fontSize: '0.75rem' }}>
            ⚡ Auto-order ON
          </span>
        )}
      </div>

      {autoOrder && (
        <div style={{
          padding: '0.75rem',
          background: 'var(--accent-light)',
          color: 'var(--accent)',
          borderRadius: '6px',
          fontSize: '0.85rem',
          marginBottom: '1rem',
        }}>
          ℹ️ Steps will be auto-reordered by recommended sequence on the server.
          Disable auto-order to use this exact order.
        </div>
      )}

      <DragDropContext onDragEnd={handleDragEnd}>
        <Droppable droppableId="pipeline">
          {(provided) => (
            <ol
              className="pipeline-list"
              {...provided.droppableProps}
              ref={provided.innerRef}
            >
              {steps.map((step, index) => (
                <Draggable key={step} draggableId={step} index={index}>
                  {(prov, snap) => (
                    <li
                      ref={prov.innerRef}
                      {...prov.draggableProps}
                      className={`pipeline-item ${snap.isDragging ? 'dragging' : ''}`}
                    >
                      <span {...prov.dragHandleProps} className="drag-handle">
                        <GripVertical size={18} />
                      </span>

                      <span className="pipeline-item-number">{index + 1}</span>
                      <span className="pipeline-item-name">{step}</span>

                      <div className="pipeline-item-controls">
                        <button
                          className="btn-icon"
                          onClick={() => moveStep(index, -1)}
                          disabled={index === 0}
                          title="Move up"
                        >
                          <ArrowUp size={16} />
                        </button>
                        <button
                          className="btn-icon"
                          onClick={() => moveStep(index, 1)}
                          disabled={index === steps.length - 1}
                          title="Move down"
                        >
                          <ArrowDown size={16} />
                        </button>
                        <button
                          className="btn-icon"
                          onClick={() => removeStep(index)}
                          title="Remove"
                          style={{ color: 'var(--error)' }}
                        >
                          <X size={16} />
                        </button>
                      </div>
                    </li>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </ol>
          )}
        </Droppable>
      </DragDropContext>
    </div>
  );
};

export default PipelineBuilder;